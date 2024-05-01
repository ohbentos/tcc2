from typing import Tuple


def set_cpus(cpus: int):
    allowed = [str(x) for x in range(cpus)]

    # subprocess.run(
    #     f"sudo systemctl set-property --runtime docker.slice AllowedCPUs={','.join(allowed)}".split(
    #         " "
    #     ),
    #     text=True,
    #     stdout=subprocess.PIPE,
    # )

    with open("/sys/fs/cgroup/server/cpuset.cpus", "w") as f:
        f.write(",".join(allowed))
    # print(f"cpus set to: {cpus}")


def set_pid_to_cgroup(pid: int, cgroup: str):
    with open(f"/sys/fs/cgroup/{cgroup}/cgroup.procs", "w") as f:
        f.write(str(pid))


def count_io_cgroups(cgroup: str) -> Tuple[int, int]:
    with open(f"/sys/fs/cgroup/{cgroup}/io.stat", "r") as f:
        content = f.read().strip("\n ").split(" ")
        return (int(content[1][7:]), int(content[2][7:]))


def read_cpu_usage(cgroup: str):
    with open(f"/sys/fs/cgroup/{cgroup}/cpu.stat", "r") as file:
        return int(file.readline()[11:])


def read_memory_stats(cgroup: str):
    try:
        with open(f"/sys/fs/cgroup/{cgroup}/memory.stat", "r") as file:
            stats = {}
            for line in file:
                key, value = line.split()
                stats[key] = int(value)

            rss_memory = stats.get("anon", 0)
            shm_memory = stats.get("shmem", 0)

            # print(f"RSS Memory Usage: {rss_memory/1_000_000} mb")
            # print(f"SHM Memory Usage: {shm_memory/1_000_000} mb")
            return rss_memory + shm_memory
    except Exception as e:
        print(f"Error reading memory stats: {e}")
        return 0
