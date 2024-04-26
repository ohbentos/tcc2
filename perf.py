import json
import multiprocessing
import os
import queue
import time
from multiprocessing import Process
from multiprocessing.synchronize import Event as EventClass
from sys import exception
from threading import Thread

import psutil

import docker
from cpuset import set_cpus
from db.postgres import PGDatabase
from monitor import count_io


def read_cgroup_stat(stat_file):
    base_path = f"/sys/fs/cgroup/docker.slice"
    try:
        with open(os.path.join(base_path, stat_file), "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File not found for {stat_file}, ensure the cgroup and PID are correct.")
    except Exception as e:
        print(f"Error reading cgroup stat: {e}")
    return "N/A"


def run_query(db: PGDatabase, query: str, done_event: EventClass):
    try:
        db.execute(query)
        db.cur.fetchall()
        db.cur.close()
        db.conn.close()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        done_event.set()


def monitor_pid(pid: int, done_event: EventClass, output_queue: queue.Queue):
    stats = []
    while not done_event.is_set():
        try:
            parent = psutil.Process(pid)
            # Get a list of all child processes recursively
            children = parent.children(recursive=True)
            processes = [parent] + children
        except psutil.NoSuchProcess:
            continue

        # Initialize CPU usage calculation for each process
        for process in processes:
            process.cpu_percent(interval=None)

        start_read_bytes = 0
        start_write_bytes = 0

        for process in processes:
            try:
                io_counter = process.io_counters()
                start_read_bytes += io_counter.read_bytes
                start_write_bytes += io_counter.write_bytes
            except:
                continue

        # Sleep a short while to measure CPU usage more accurately
        time.sleep(0.1)

        total_cpu_usage = 0
        total_memory_usage = 0

        for process in processes:
            try:
                # Aggregate the CPU usage and memory usage of each process
                io_counter = process.io_counters()
                total_cpu_usage += process.cpu_percent(interval=None)
                total_memory_usage += process.memory_info().rss  # RSS memory in bytes
            except psutil.NoSuchProcess:
                continue  # The process has ended or doesn't exist anymore

        # stats.append((total_cpu_usage, total_memory_usage))
        stats.append({"cpu": total_cpu_usage, "mem": total_memory_usage})
        # return total_cpu_usage, total_memory_usage
    output_queue.put(("server_perf", stats))


# def monitor_cgroups(done_event: EventClass, output_queue: queue.Queue):
#     cgroup_stats = []
#     # cpus = psutil.cpu_percent(percpu=True, interval=None)[0:-2]
#     try:
#         while not done_event.is_set():
#             cpu_usage = read_cgroup_stat("cpu.max")
#             cpus = psutil.cpu_percent(percpu=True, interval=None)[0:-2]
#             memory_usage = read_cgroup_stat("memory.current")
#             cgroup_stats.append((cpu_usage, memory_usage, cpus))
#             time.sleep(0.1)  # sleep for a short time to limit the frequency of reads
#     except Exception as e:
#         print(f"Error during cgroup monitoring: {e}")
#     finally:
#         output_queue.put(("server_perf", cgroup_stats))


def monitor_process(
    process: Process, done_event: EventClass, output_queue: queue.Queue
):
    usage_stats = []
    ps = psutil.Process(process.pid)
    try:
        while not done_event.is_set():
            cpu_usage = ps.cpu_percent(interval=0.1)
            memory_usage = ps.memory_info().rss  # in bytes
            # usage_stats.append((cpu_usage, memory_usage))
            usage_stats.append({"cpu": cpu_usage, "mem": memory_usage})
    except psutil.NoSuchProcess:
        pass
        # print("No such process found.")
    finally:
        output_queue.put(("client_perf", usage_stats))


def test_db(db_name: str, query: str, test_name: str, cpu_count: int):
    # Start the database query in a separate process
    # execute a command

    dclient = docker.from_env()
    containers = dclient.containers.list()

    cont = {}
    pid = 0
    for x in containers:
        if x.attrs == None:
            print("ERROR")
            exit(0)
        state = x.attrs["State"]
        running = state["Running"]
        pid = state["Pid"]

        if running == True:
            name = x.attrs["Name"][1:]
            cont[name] = {}
            cont[name]["id"] = x.id
            cont[name]["port"] = x.attrs["HostConfig"]["PortBindings"]["5432/tcp"][0][
                "HostPort"
            ]
            cont[name]["pid"] = pid

    # print(psutil.cpu_percent(percpu=True)[0:-2])
    # exit(0)

    db_info = cont[db_name]
    db = PGDatabase(int(db_info["port"]))
    db.start()

    done_event = multiprocessing.Event()

    query_process = multiprocessing.Process(
        target=run_query,
        args=(
            (db),
            (query),
            (done_event),
        ),
    )

    initial_io = count_io(pid)

    query_start = time.time()
    query_process.start()

    results_queue = queue.Queue()  # Queue to collect results from threads

    client_perf_thread = Thread(
        target=monitor_process, args=(query_process, done_event, results_queue)
    )
    # cgroup_thread = Thread(target=monitor_cgroups, args=(done_event, results_queue))
    server_perf_thread = Thread(
        target=monitor_pid, args=(pid, done_event, results_queue)
    )

    client_perf_thread.start()
    server_perf_thread.start()

    query_process.join()
    query_execution_time = time.time() - query_start
    client_perf_thread.join()
    server_perf_thread.join()

    results = {}
    while not results_queue.empty():
        identifier, data = results_queue.get()
        results[identifier] = data

    final_io = count_io(pid)

    read_bytes = final_io[0] - initial_io[0]
    write_bytes = final_io[1] - initial_io[1]

    results["io"] = {"read": read_bytes, "write": write_bytes}
    results["time"] = query_execution_time

    file_name = f"./results/{db_name}/{cpu_count}/{run}_{test_name}_{query}.json"

    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w") as f:
        json.dump(results, f)

    # print("Client Performance:", results["client_perf"])
    # print("Server Performance:", json.dumps(results["server_perf"]))
    # print("IO Performance:", (read_bytes, write_bytes))
    # print("time:", query_execution_time)


if __name__ == "__main__":
    tests = {
        "graph_unified": {
            "get_all_graph_properties": [
                "SELECT * from graphs LIMIT 1",
                "SELECT * from graphs LIMIT 10",
                "SELECT * from graphs LIMIT 100",
                "SELECT * from graphs LIMIT 1000",
                "SELECT * from graphs LIMIT 10000",
                "SELECT * from graphs LIMIT 100000",
                "SELECT * from graphs LIMIT 1000000",
            ],
            "get_only_graph_properties": [
                "SELECT graph_id,"

            ],
        }
    }

    MAX_RUNS = 5

    for cpus in range(1, 9):
        set_cpus(cpus)
        time.sleep(5)

        for run in range(0, MAX_RUNS):
            for test in tests:
                for query in tests[test]["get_all_graph_properties"]:
                    print(f"{run} testing {test} with {cpus} cpus on query {query}")
                    test_db(test, query, "get_all_graph_properties", cpus)
                    time.sleep(5)
