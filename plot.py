import json

import matplotlib.pyplot as plt


def stats_to_str(stats: dict, divide=1) -> str:
    s = f"""mean    : {stats["mean"]/divide:.2f}
median  : {stats["median"]/divide:.2f}
min     : {stats["min"]/divide:.2f}
max     : {stats["max"]/divide:.2f}
samples : {stats["samples"]}
std_dev : {stats["std_deviation"]/divide:.2f}
perc_99 : {stats["perc_99"]/divide:.2f}
perc_95 : {stats["perc_95"]/divide:.2f}
perc_90 : {stats["perc_90"]/divide:.2f}
perc_75 : {stats["perc_75"]/divide:.2f}
perc_50 : {stats["perc_50"]/divide:.2f}"""
    return s


def save_plot(file_name: str, run_config: dict):
    with open(
        file_name,
        "r",
    ) as f:
        fig, axs = plt.subplots(2, 2, figsize=(16, 10))

        test_name = run_config["test_name"]
        test_id = run_config["test_id"]
        cpu_count = run_config["cpu_count"]
        db_name = run_config["db_name"]
        run_number = run_config["run_number"]
        test_id = run_config["test_id"]

        fig.suptitle(
            f"Run:{run_number} Name:{db_name} Test:{test_name}-{test_id} CPUs:{cpu_count}",
            fontsize=16,
        )

        plt.subplots()
        plt_server_cpu = axs[0, 0]
        plt_server_mem = axs[1, 0]

        plt_client_cpu = axs[0, 1]
        plt_client_mem = axs[1, 1]

        result = json.load(f)

        interval = float(result["interval"])

        server_stats = result["server"]["stats"]
        client_stats = result["client"]["stats"]

        server_stats_cpu = server_stats["cpu"]
        server_stats_mem = server_stats["mem"]

        client_stats_cpu = client_stats["cpu"]
        client_stats_mem = client_stats["mem"]

        # cpu server
        plt_server_cpu.plot(
            [x * interval for x in range(len(result["server"]["samples"]))],
            [x["cpu"] for x in result["server"]["samples"]],
        )
        plt_server_cpu.set_ylabel("CPU%")
        plt_server_cpu.set_xlabel("time (seconds)")
        plt_server_cpu.grid()
        fig.text(
            0,
            1,
            stats_to_str(server_stats_cpu),
            va="top",
            ha="left",
            transform=fig.transFigure,
        )
        plt_server_cpu.set_title("Server CPU Usage")

        # mem server
        plt_server_mem.plot(
            [x * interval for x in range(len(result["server"]["samples"]))],
            [x["mem"] / 1_000_000 for x in result["server"]["samples"]],
        )
        plt_server_mem.set_ylabel("Memory (MB)")
        plt_server_mem.set_xlabel("time (seconds)")
        plt_server_mem.grid()
        fig.text(
            0,
            0,
            stats_to_str(server_stats_mem, divide=1_000_000),
            va="bottom",
            ha="left",
            transform=fig.transFigure,
        )
        plt_server_mem.set_title("Server Memory Usage")

        # cpu client
        plt_client_cpu.plot(
            [x * interval for x in range(len(result["client"]["samples"]))],
            [x["cpu"] for x in result["client"]["samples"]],
        )
        plt_client_cpu.set_ylabel("CPU%")
        plt_client_cpu.set_xlabel("time (seconds)")
        plt_client_cpu.grid()
        fig.text(
            1,
            1,
            stats_to_str(client_stats_cpu),
            va="top",
            ha="right",
            transform=fig.transFigure,
        )
        plt_client_cpu.set_title("Client Cpu Usage")

        # mem client
        plt_client_mem.plot(
            [x * interval for x in range(len(result["client"]["samples"]))],
            [x["mem"] / 1_000_000 for x in result["client"]["samples"]],
        )
        plt_client_mem.set_ylabel("Memory (MB)")
        plt_client_mem.set_xlabel("time (seconds)")
        plt_client_mem.grid()
        fig.text(
            1,
            0,
            stats_to_str(client_stats_mem, divide=1_000_000),
            va="bottom",
            ha="right",
            transform=fig.transFigure,
        )
        plt_client_mem.set_title("Client Memory Usage")

        plt.tight_layout()
        fig.savefig(file_name.replace(".json", ".png"))

        # plt_client_cpu.cla()
        # plt_client_mem.cla()
        # plt_server_cpu.cla()
        # plt_server_mem.cla()

        # fig.clf()
        # plt.close(fig)
        plt.close("all")
