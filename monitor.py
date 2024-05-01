import time
from multiprocessing import Queue
from multiprocessing.synchronize import Event

from cgroups import read_cpu_usage, read_memory_stats

SLEEP_TIME = 0.05


def monitor_cgroup(
    cgroup: str, done_event: Event, output_queue: Queue, lets_go: Event, cpus: int
):
    global SLEEP_TIME

    lets_go.wait()

    stats = []
    print(f"Starting to monitor {cgroup} perf")
    while not done_event.is_set():
        initial_cpu_usage = read_cpu_usage(cgroup)

        time.sleep(SLEEP_TIME)  # Sleep for the calculated duration

        final_cpu_usage = read_cpu_usage(cgroup)

        delta_usage = final_cpu_usage - initial_cpu_usage
        delta_time = (SLEEP_TIME) * 1_000_000  # seconds to microseconds
        cpu_percentage = delta_usage / delta_time * 100

        memory_usage = read_memory_stats(cgroup)

        s = {
            "cpu": min(cpu_percentage, cpus * 100),
            "mem": memory_usage,
        }
        stats.append(s)

    print(f"Exiting {cgroup} perf")
    output_queue.put(stats)
