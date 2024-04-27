import json
import multiprocessing
import os
import time
from multiprocessing import Queue
from multiprocessing.synchronize import Event

import docker
from db.postgres import PGDatabase
from monitor import (SLEEP_TIME, count_io_cgroups, monitor_pid,
                     monitor_python_process)
from statistic import calculate_statistics


def run_query(db: PGDatabase, query: str, done_event: Event):
    try:
        db.execute(query)
        db.cur.fetchall()
        db.cur.close()
        db.conn.close()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        print("exiting run_query")
        done_event.set()


def test_db(db_name: str, query: str, test_name: str | None, cpu_count: int, run: int):

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

    db_info = cont[db_name]
    db = PGDatabase(int(db_info["port"]))

    db.start()

    done_event = multiprocessing.Event()
    server_results_queue = Queue()  # Queue to collect results from threads
    client_results_queue = Queue()  # Queue to collect results from threads

    query_process = multiprocessing.Process(
        target=run_query,
        args=(
            (db),
            (query),
            (done_event),
        ),
        daemon=True,
    )
    client_perf_process = multiprocessing.Process(
        target=monitor_python_process,
        args=(query_process, done_event, client_results_queue),
        daemon=True,
    )
    client_perf_process.daemon
    server_perf_process = multiprocessing.Process(
        target=monitor_pid,
        args=(pid, done_event, server_results_queue),
        daemon=True,
    )

    initial_io = count_io_cgroups()

    query_start = time.time()
    query_process.start()

    client_perf_process.start()
    server_perf_process.start()

    query_process.join()
    query_execution_time = time.time() - query_start
    client_perf_process.join()
    server_perf_process.join()

    results = {}
    data = server_results_queue.get()
    results["server"] = {
        "samples": data,
        "stats": calculate_statistics(data),
    }
    data = client_results_queue.get()
    results["client"] = {
        "samples": data,
        "stats": calculate_statistics(data),
    }

    final_io = count_io_cgroups()

    read_bytes = final_io[0] - initial_io[0]
    write_bytes = final_io[1] - initial_io[1]

    results["io"] = {"read": read_bytes, "write": write_bytes}
    results["time"] = query_execution_time
    results["interval"] = SLEEP_TIME

    if test_name is not None:
        file_name = f"./results/{db_name}/{cpu_count}/{run}_{test_name}_{query}.json"

        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, "w") as f:
            json.dump(results, f)
            print(f"Results saved to:\n{file_name.replace(' ','\\ ').replace('*','\\*').replace('?','\\?')}")

    # print("Client Performance:", results["client_perf"])
    # print("Server Performance:", json.dumps(results["server_perf"]))
    # print("IO Performance:", (read_bytes, write_bytes))
    # print("time:", query_execution_time)


if __name__ == "__main__":
    test_db(
        "graph", "select * from graphs LIMIT 10000", "get_all_graph_properties", 0, 0
    )
    # tests = {
    #     "graph_unified": {
    #         "get_all_graph_properties": [
    #             "SELECT * from graphs LIMIT 1",
    #             "SELECT * from graphs LIMIT 10",
    #             "SELECT * from graphs LIMIT 100",
    #             "SELECT * from graphs LIMIT 1000",
    #             "SELECT * from graphs LIMIT 10000",
    #             "SELECT * from graphs LIMIT 100000",
    #             "SELECT * from graphs LIMIT 1000000",
    #         ],
    #         "get_only_graph_properties": ["SELECT graph_id,"],
    #     }
    # }

    # MAX_RUNS = 5

    # for cpus in range(1, 9):
    #     set_cpus(cpus)
    #     time.sleep(5)

    #     for run in range(0, MAX_RUNS):
    #         for test in tests:
    #             for query in tests[test]["get_all_graph_properties"]:
    #                 print(f"{run} testing {test} with {cpus} cpus on query {query}")
    #                 test_db(test, query, "get_all_graph_properties", cpus)
    #                 time.sleep(5)
