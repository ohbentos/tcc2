import json

import matplotlib.pyplot as plt

with open(
    "./results/graph/0/0_get_all_graph_properties_select * from graphs LIMIT 10000.json",
    "r",
) as f:
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    plt.subplots()
    plt_server_cpu = axs[0, 0]
    plt_server_mem = axs[1, 0]

    plt_client_cpu = axs[0, 1]
    plt_client_mem = axs[1, 1]

    result = json.load(f)

    plt_server_cpu.plot(
        [x * 0.1 for x in range(len(result["server"]["samples"]))],
        [x["cpu"] for x in result["server"]["samples"]],
    )
    plt_server_cpu.set_ylabel("CPU%")
    plt_server_cpu.set_xlabel("time (seconds)")
    plt_server_cpu.grid()
    # plt.axhline(
    #     result["server"]["stats"]["cpu"]["mean"],
    #     color="k",
    #     linestyle="dashed",
    #     linewidth=1,
    # )

    plt_server_mem.plot(
        [x * 0.1 for x in range(len(result["server"]["samples"]))],
        [x["mem"] / 1_000_000 for x in result["server"]["samples"]],
    )
    plt_server_mem.set_ylabel("Memory (MB)")
    plt_server_mem.set_xlabel("time (seconds)")
    plt_server_mem.grid()

    plt_client_cpu.plot(
        [x * 0.1 for x in range(len(result["client"]["samples"]))],
        [x["cpu"] for x in result["client"]["samples"]],
    )
    plt_client_cpu.set_ylabel("CPU%")
    plt_client_cpu.set_xlabel("time (seconds)")
    plt_client_cpu.grid()

    plt_client_mem.plot(
        [x * 0.1 for x in range(len(result["client"]["samples"]))],
        [x["mem"] / 1_000_000 for x in result["client"]["samples"]],
    )
    plt_client_mem.set_ylabel("Memory (MB)")
    plt_client_mem.set_xlabel("time (seconds)")
    plt_client_mem.grid()

    # plt.ylabel("CPU%")
    # plt.grid()
    # plt.axhline(
    #     result["server"]["stats"]["cpu"]["mean"],
    #     color="k",
    #     linestyle="dashed",
    #     linewidth=1,
    # )
    # plt.xlabel("time (seconds)")

    fig.savefig("my_plot.png")
