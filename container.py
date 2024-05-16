import sys

import docker


def get_container_port(container_name: str):
    if container_name.startswith("graph"):
        return "5432/tcp"
    elif container_name.startswith("neo4j"):
        return "7687/tcp"
    else:
        raise ValueError("Invalid container name")


def get_container_info(container_name: str):
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
            try:
                key = get_container_port(container_name)
                host_port = x.attrs["NetworkSettings"]["Ports"][key][0]["HostPort"]
            except IndexError:
                continue
            cont[name]["port"] = int(host_port)
            cont[name]["pid"] = int(pid)

    db_info = cont[container_name]
    return db_info


if __name__ == "__main__":
    get_container_info(sys.argv[1])
