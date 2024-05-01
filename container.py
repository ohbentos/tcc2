import docker


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
                host_port = list(x.attrs["HostConfig"]["PortBindings"].values())[0][0][
                    "HostPort"
                ]
            except IndexError:
                continue
            cont[name]["port"] = int(host_port)
            cont[name]["pid"] = int(pid)

    db_info = cont[container_name]
    return db_info
