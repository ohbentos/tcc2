import subprocess


def set_cpus(cpus: int):
    allowed = [str(x) for x in range(cpus)]

    subprocess.run(
        f"sudo systemctl set-property --runtime docker.slice AllowedCPUs={','.join(allowed)}".split(
            " "
        ),
        text=True,
        stdout=subprocess.PIPE,
    )

    # with open("/sys/fs/cgroup/docker.slice/cpuset.cpus", "r") as f:
    print(f"cpus set to: {cpus}")
