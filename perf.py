import json
import multiprocessing
import os
import time
from multiprocessing import Queue
from multiprocessing.synchronize import Event

from container import get_container_info
from cpuset import set_cpus
from db.postgres import PGDatabase
from monitor import (SLEEP_TIME, count_io_cgroups, monitor_pid,
                     monitor_python_process)
from plot import save_plot
from statistic import calculate_statistics
from tests import get_tests


def run_query(db: PGDatabase, query: str, done_event: Event, queue: Queue):
    try:
        db.execute(query)
        records = db.cur.fetchall()
        queue.put(len(records) or 0)
        db.cur.close()
        db.conn.close()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        print("exiting run_query")
        done_event.set()


def test_db(
    db_name: str,
    query: str,
    query_id: str,
    test_name: str | None,
    cpu_count: int,
    run: int,
):
    db_info = get_container_info(db_name)
    db = PGDatabase(db_info["port"])
    pid = db_info["pid"]

    db.start()

    done_event = multiprocessing.Event()

    query_result_queue = Queue()
    server_results_queue = Queue()  # Queue to collect results from threads
    client_results_queue = Queue()  # Queue to collect results from threads

    query_process = multiprocessing.Process(
        target=run_query,
        args=(db, query, done_event, query_result_queue),
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
    results["records"] = query_result_queue.get()
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
    results["run_config"] = {
        "db_name": db_name,
        "cpu_count": cpu_count,
        "run_number": run,
        "query": query,
        "test_name": test_name,
        "test_id": query_id,
    }

    if test_name is not None:
        file_name = f"./results/{db_name}/{cpu_count}/{run}_{query_id}_{test_name}-{query_id}.json"

        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, "w") as f:
            json.dump(results, f)
            print(f"Results saved to:\n{file_name}")
            print("Query execution time: ", query_execution_time)

        print("saving plot")
        save_plot(file_name, results["run_config"])
        print("plot saved")


if __name__ == "__main__":
    dbs_test = ["graph_unified"]

    MAX_RUNS = 3
    for db_name in dbs_test:
        tests = get_tests(db_name)
        for cpus in range(1, 9):
            set_cpus(cpus)
            time.sleep(0.250)

            for run in range(1, MAX_RUNS + 1):
                for test_name in tests:
                    for query in tests[test_name]:
                        q = list(query.keys())[0]
                        qid = list(query.values())[0]
                        print(
                            f"{run} testing db {db_name} on test {test_name} with {cpus} cpus on query {qid}-{q}"
                        )
                        test_db(db_name, q, qid, test_name, cpus, run)
                        print("\n")
