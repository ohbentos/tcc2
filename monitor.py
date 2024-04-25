import time
from typing import Tuple

import psutil


def get_total_cpu_and_memory_usage(pid):
    """Calculate the total CPU and memory usage (RSS) for a process and its child processes."""
    try:
        parent = psutil.Process(pid)
        # Get a list of all child processes recursively
        children = parent.children(recursive=True)
        processes = [parent] + children
    except psutil.NoSuchProcess:
        return "No such process with PID: {}".format(pid), None

    # Initialize CPU usage calculation for each process
    for process in processes:
        process.cpu_percent(interval=None)

    # Sleep a short while to measure CPU usage more accurately
    time.sleep(0.1)

    total_cpu_usage = 0
    total_memory_usage = 0
    for process in processes:
        try:
            # Aggregate the CPU usage and memory usage of each process
            total_cpu_usage += process.cpu_percent(interval=None)
            total_memory_usage += process.memory_info().rss  # RSS memory in bytes
        except psutil.NoSuchProcess:
            continue  # The process has ended or doesn't exist anymore

    return total_cpu_usage, total_memory_usage


def monitor_cpu_memory_usage(pid, interval=0.1):
    """Monitor CPU and memory usage of a process and its children, printing it every 'interval' seconds."""
    try:
        while True:
            total_cpu, total_memory = get_total_cpu_and_memory_usage(pid)
            print(f"Total CPU usage: {total_cpu}%")
            print(
                f"Total Memory usage: {total_memory  / (1024 ** 2):.2f} MB"
            )  # Convert bytes to MB
            time.sleep(interval)  # Wait for 'interval' seconds before the next check
    except KeyboardInterrupt:
        print("Monitoring stopped.")


# Example usage
# process_id = 554397  # Replace 1234 with the PID of your process
# print(monitor_cpu_memory_usage(process_id))


def count_io(pid: int) -> Tuple[int, int]:
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        processes = [parent] + children

        total_read = 0
        total_write = 0
        for process in processes:
            io_counters = process.io_counters()
            total_read += io_counters.read_bytes
            total_write += io_counters.write_bytes

        return (total_read, total_write)
    except:
        return (0, 0)
