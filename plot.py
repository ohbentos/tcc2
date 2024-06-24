import json
import os
import sys
from collections.abc import Hashable
from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd

ROOT_DIR = "results"
DEFAULT_DPI = 200


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
            f"Run:{run_number} Name:{db_name} Test:{test_name} Limit:{test_id} CPUs:{cpu_count}",
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
        fig.savefig(file_name.replace(".json", ".png"), dpi=50)

        # plt_client_cpu.cla()
        # plt_client_mem.cla()
        # plt_server_cpu.cla()
        # plt_server_mem.cla()

        # fig.clf()
        # plt.close(fig)
        plt.close("all")


def read_json_data(root_dir: str) -> pd.DataFrame:
    data = []

    for db_name in os.listdir(root_dir):
        db_path = os.path.join(root_dir, db_name)
        if os.path.isdir(db_path):
            for cpu_count in os.listdir(db_path):
                cpu_path = os.path.join(db_path, cpu_count)
                if os.path.isdir(cpu_path):
                    for file_name in os.listdir(cpu_path):
                        if file_name.endswith(".json"):
                            file_path = os.path.join(cpu_path, file_name)
                            with open(file_path, "r") as file:
                                # if not file.name.endswith("-None.json"):
                                #     continue
                                json_data = json.load(file)

                                run_config = json_data.get("run_config")
                                test_name = run_config.get("test_name")
                                run_number = run_config.get("run_number")
                                test_id = run_config.get("test_id")

                                server_stats = json_data.get("server", {}).get(
                                    "stats", {}
                                )
                                client_stats = json_data.get("client", {}).get(
                                    "stats", {}
                                )

                                # server_mem_mean = server_stats.get("mem", {}).get("mean")
                                # server_cpu_mean = server_stats.get("cpu", {}).get("mean")

                                server_mem = server_stats.get("mem", {})
                                server_cpu = server_stats.get("cpu", {})

                                client_mem = client_stats.get("mem", {})
                                client_cpu = client_stats.get("cpu", {})

                                # client_cpu_mean = client_cpu.get("mean")
                                # client_mem_mean = client_mem.get("mean")

                                time = json_data.get("time")

                                data.append(
                                    {
                                        "Test Name": test_name,
                                        "Limit": test_id or "None",
                                        "Database": db_name,
                                        "CPUs": cpu_count,
                                        "Time": time,
                                        "Server CPU Mean": server_cpu["mean"],
                                        "Server CPU Median": server_cpu["median"],
                                        "Server CPU Max": server_cpu["max"],
                                        "Server CPU Min": server_cpu["min"],
                                        "Server CPU Std": server_cpu["std_deviation"],
                                        "Server Memory Mean": server_mem["mean"]
                                        / 1_000_000,
                                        "Server Memory Median": server_mem["median"]
                                        / 1_000_000,
                                        "Server Memory Max": server_mem["max"]
                                        / 1_000_000,
                                        "Server Memory Min": server_mem["min"]
                                        / 1_000_000,
                                        "Server Memory Std": server_mem["std_deviation"]
                                        / 1_000_000,
                                        "Client CPU Mean": client_cpu["mean"],
                                        "Client CPU Median": client_cpu["median"],
                                        "Client CPU Max": client_cpu["max"],
                                        "Client CPU Min": client_cpu["min"],
                                        "Client CPU Std": client_cpu["std_deviation"],
                                        "Client Memory Mean": client_mem["mean"]
                                        / 1_000_000,
                                        "Client Memory Median": client_mem["median"]
                                        / 1_000_000,
                                        "Client Memory Max": client_mem["max"]
                                        / 1_000_000,
                                        "Client Memory Min": client_mem["min"]
                                        / 1_000_000,
                                        "Client Memory Std": client_mem["std_deviation"]
                                        / 1_000_000,
                                    }
                                )

    return pd.DataFrame(data)


def aggregate_data(df: pd.DataFrame):
    agg_df = (
        df.groupby(["Test Name", "Limit", "Database", "CPUs"])
        .mean()
        .reset_index()
        .sort_values(by=["Test Name", "CPUs", "Limit"])
    )
    print(agg_df)

    return agg_df


def plot(
    df: pd.DataFrame,
    t: Literal["Server", "Client"],
    dpi: int,
    location: str = "",
):
    df["CPUs"] = df["CPUs"].astype(int)
    df[f"{t} CPU Mean"] = df[f"{t} CPU Mean"].astype(float)

    database_colors = {
        "graph_edge": "blue",
        "graph_jsonb": "green",
        "graph_three": "red",
        "graph_three_idx": "magenta",
        "graph_unified": "orange",
        "graph_vertice": "purple",
        "mongodb_unified": "cyan",
        "neo4j_separated": "yellow",
        "neo4j_unified": "black",
        "postgres_edge": "blue",
        "postgres_jsonb": "green",
        "postgres_three": "red",
        "postgres_three_idx": "magenta",
        "postgres_unified": "orange",
        "postgres_vertice": "purple",
    }

    grouped = df.groupby("Test Name")

    for test_name, group in grouped:
        unique_limits = group["Limit"].unique()
        num_limits = len(unique_limits)
        fig, axs = plt.subplots(
            num_limits, 3, figsize=(18, 6 * num_limits), squeeze=False
        )
        fig.suptitle(t)
        for i, limit in enumerate(unique_limits):
            axs[i, 0].set_title(f"Test Name: {test_name}, Limit: {limit}")
            axs[i, 0].set_ylabel("Mean CPU Usage")
            axs[i, 1].set_ylabel("Mean Memory Usage(MB)")
            axs[i, 2].set_ylabel("Time(s)")
            for (database), database_group in group[group["Limit"] == limit].groupby(
                "Database"
            ):
                if not isinstance(database, Hashable):
                    continue
                database = str(database)
                axs[i, 0].plot(
                    database_group["CPUs"],
                    database_group[f"{t} CPU Mean"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"{database}",
                )
                axs[i, 1].plot(
                    database_group["CPUs"],
                    database_group[f"{t} Memory Mean"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"{database}",
                )
                axs[i, 2].plot(
                    database_group["CPUs"],
                    database_group["Time"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"{database}",
                )
            axs[i, 0].set_xlabel("Number of CPUs")
            axs[i, 1].set_xlabel("Number of CPUs")
            axs[i, 2].set_xlabel("Number of CPUs")
            axs[i, 0].set_xticks(range(1, 9))
            axs[i, 1].set_xticks(range(1, 9))
            axs[i, 2].set_xticks(range(1, 9))
            axs[i, 0].legend()
            axs[i, 1].legend()
            axs[i, 2].legend()
            axs[i, 0].grid(True)
            axs[i, 1].grid(True)
            axs[i, 2].grid(True)
        plt.tight_layout()
        if location:
            os.makedirs(f"plots_{dpi}/{location}", exist_ok=True)
            plt.savefig(
                f"plots_{dpi}/{location}/{t.lower()}_{test_name}.png",
                dpi=dpi,
            )
        else:
            plt.savefig(f"plots_{dpi}/{t.lower()}_{test_name}.png", dpi=dpi)
        plt.close()


if __name__ == "__main__":
    dpi = DEFAULT_DPI
    if len(sys.argv) == 2:
        dpi = int(sys.argv[1])
    elif len(sys.argv) > 2:
        print("Usage: python plot.py [dpi]")
        sys.exit(1)

    print(f"DPI: {dpi}")

    df = read_json_data(ROOT_DIR)
    df["Database"] = df["Database"].str.replace("^graph_", "postgres_", regex=True)

    df.to_csv("total_benchmark_results.csv", index=False)
    df.to_excel("total_benchmark_results.xlsx", index=False)

    agg_df = aggregate_data(df).copy()

    agg_df.to_csv("agg_benchmark_results.csv", index=False)
    agg_df.to_excel("agg_benchmark_results.xlsx", index=False)

    plot(agg_df, "Server", dpi, "all")
    plot(agg_df, "Client", dpi, "all")

    # mongodb_data = agg_df[agg_df["Database"].str.startswith("mongodb")].copy()
    # plot(mongodb_data, "Server", dpi, "mongodb")  # type:ignore
    # plot(mongodb_data, "Client", dpi, "mongodb")  # type:ignore

    # neo4j_data = agg_df[agg_df["Database"].str.startswith("neo4j")].copy()
    # plot(neo4j_data, "Server", dpi, "neo4j")  # type:ignore
    # plot(neo4j_data, "Client", dpi, "neo4j")  # type:ignore

    # postgres_data = agg_df[agg_df["Database"].str.startswith("graph")].copy()
    # plot(postgres_data, "Server", dpi, "postgres")  # type:ignore
    # plot(postgres_data, "Client", dpi, "postgres")  # type:ignore
