import time
from multiprocessing import Process, Queue
from multiprocessing.synchronize import Event
from typing import Tuple

import psutil

from pid import PID

SLEEP_TIME = 0.05

CGROUP_PATH = "/sys/fs/cgroup/docker.slice"


import time

import psutil


def monitor_pid(pid: int, done_event, output_queue):
    global SLEEP_TIME, CGROUP_PATH

    stats = []
    print("Starting to monitor server perf")
    while not done_event.is_set():
        loop_start_time = time.time_ns()  # Record the start time of the loop
        try:
            parent = psutil.Process(pid)
            # Get a list of all child processes recursively
            children = parent.children(recursive=True)
            processes = [parent] + children
        except psutil.NoSuchProcess:
            continue

        # Initialize CPU usage calculation for each process
        for process in processes:
            try:
                process.cpu_percent(interval=None)  # Immediate call to start measuring
            except psutil.NoSuchProcess:
                continue
        initial_cpu_usage = read_cpu_usage(CGROUP_PATH)

        # Calculate how much time to sleep by subtracting the elapsed time from SLEEP_TIME
        elapsed_time = time.time_ns() - loop_start_time
        sleep_time = max(
            0, SLEEP_TIME - (elapsed_time / 1_000_000_000)
        )  # Ensure sleep_time is not negative
        time.sleep(sleep_time)  # Sleep for the calculated duration

        final_cpu_usage = read_cpu_usage(CGROUP_PATH)
        delta_usage = final_cpu_usage - initial_cpu_usage
        delta_time = SLEEP_TIME * 1_000_000  # seconds to microseconds
        cpu_percentage = delta_usage / delta_time * 100
        total_memory_usage = 0

        for process in processes:
            try:
                total_memory_usage += process.memory_info().rss  # RSS memory in bytes
            except (
                psutil.NoSuchProcess
            ):  # The process has ended or doesn't exist anymore
                continue

        s = {"cpu": cpu_percentage, "mem": total_memory_usage}
        stats.append(s)

    print("Exiting server perf")
    output_queue.put(stats)


def count_io_cgroups() -> Tuple[int, int]:
    with open("/sys/fs/cgroup/docker.slice/io.stat", "r") as f:
        content = f.read().strip("\n ").split(" ")
        return (int(content[1][7:]), int(content[2][7:]))


def monitor_python_process(process: Process, done_event: Event, output_queue: Queue):
    global PID, SLEEP_TIME

    usage_stats = []
    print("Starting to monitor client perf")

    try:
        ps = psutil.Process(process.pid)
    except psutil.NoSuchProcess:
        output_queue.put(usage_stats)
        print("Exiting client perf2")
        return

    PID = process.pid
    while not done_event.is_set():
        start_time = time.time()  # Record the start time of the monitoring
        try:
            cpu_usage = ps.cpu_percent(interval=None)
            memory_usage = ps.memory_info().rss  # in bytes
        except psutil.NoSuchProcess:
            continue
        usage_stats.append({"cpu": cpu_usage, "mem": memory_usage})

        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        remaining_sleep_time = max(
            0, SLEEP_TIME - elapsed_time
        )  # Calculate the remaining time to sleep
        time.sleep(remaining_sleep_time)  # Sleep only for the remaining time

        print("Exiting client perf")
        output_queue.put(usage_stats)


def read_cpu_usage(cgroup_path):
    """
    Read CPU usage in microseconds from the cgroup cpu.stat file.
    """
    with open(f"{cgroup_path}/cpu.stat", "r") as file:
        return int(file.readline()[11:])
