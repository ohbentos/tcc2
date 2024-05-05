import json
import os

import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import Literal

ROOT_DIR = "results"


def read_json_data(root_dir: str) -> pd.DataFrame:
    data = []

    # Traverse through the directory structure
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
                                json_data = json.load(file)
                                # Extract required data
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
                                # Append data to list
                                data.append(
                                    {
                                        "Test Name": test_name,
                                        "Limit": test_id,
                                        "Database": db_name,
                                        "CPUs": cpu_count,
                                        "Time": time,
                                        "Server CPU Mean": server_cpu["mean"],
                                        "Server CPU Median": server_cpu["median"],
                                        "Server CPU Max": server_cpu["max"],
                                        "Server CPU Min": server_cpu["min"],
                                        "Server CPU Std": server_cpu["std_deviation"],
                                        "Server Memory Mean": server_mem["mean"],
                                        "Server Memory Median": server_mem["median"],
                                        "Server Memory Max": server_mem["max"],
                                        "Server Memory Min": server_mem["min"],
                                        "Server Memory Std": server_mem[
                                            "std_deviation"
                                        ],
                                        "Client CPU Mean": client_cpu["mean"],
                                        "Client CPU Median": client_cpu["median"],
                                        "Client CPU Max": client_cpu["max"],
                                        "Client CPU Min": client_cpu["min"],
                                        "Client CPU Std": client_cpu["std_deviation"],
                                        "Client Memory Mean": client_mem["mean"],
                                        "Client Memory Median": client_mem["median"],
                                        "Client Memory Max": client_mem["max"],
                                        "Client Memory Min": client_mem["min"],
                                        "Client Memory Std": client_mem[
                                            "std_deviation"
                                        ],
                                    }
                                )

    return pd.DataFrame(data)


def aggregate_data(df: pd.DataFrame):
    # Group by Database, CPUs, and Test Name, then calculate mean
    agg_df = (
        df.groupby(["Test Name", "Limit", "Database", "CPUs"])
        .mean()
        .reset_index()
        .sort_values(by=["Test Name", "CPUs", "Limit"])
    )

    return agg_df


def plot(df: pd.DataFrame, t: Literal["Server", "Client"]):
    df["CPUs"] = df["CPUs"].astype(int)
    df[f"{t} CPU Mean"] = df[f"{t} CPU Mean"].astype(float)

    database_colors = {
        "graph_edge": "blue",
        "graph_jsonb": "green",
        "graph_three": "red",
        "graph_unified": "orange",
        "graph_vertice": "purple",
    }

    # Group by Test Name
    grouped = df.groupby("Test Name")

    for test_name, group in grouped:
        unique_limits = group["Limit"].unique()
        num_plots = len(unique_limits)
        fig, axs = plt.subplots(num_plots, 3, figsize=(18, 6 * num_plots))
        if num_plots == 1:
            axs = [axs]  # Ensure axs is always a list of axes
        for i, limit in enumerate(unique_limits):
            axs[i, 0].set_title(f"Test Name: {test_name}, Limit: {limit}")
            axs[i, 0].set_ylabel("Mean CPU Usage")
            axs[i, 1].set_ylabel("Mean Memory Usage")
            axs[i, 2].set_ylabel("Time")
            for (database), database_group in group[group["Limit"] == limit].groupby(
                "Database"
            ):
                axs[i, 0].plot(
                    database_group["CPUs"],
                    database_group[f"{t} CPU Mean"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"Database: {database}",
                )
                axs[i, 1].plot(
                    database_group["CPUs"],
                    database_group[f"{t} Memory Mean"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"Database: {database}",
                )
                axs[i, 2].plot(
                    database_group["CPUs"],
                    database_group["Time"],
                    marker="o",
                    linestyle="-",
                    color=database_colors[database],
                    label=f"Database: {database}",
                )
            axs[i, 0].set_xlabel("Number of CPUs")
            axs[i, 1].set_xlabel("Number of CPUs")
            axs[i, 2].set_xlabel("Number of CPUs")
            axs[i, 0].set_xticks(range(1, 9))  # assuming 1 to 8 CPUs
            axs[i, 1].set_xticks(range(1, 9))  # assuming 1 to 8 CPUs
            axs[i, 2].set_xticks(range(1, 9))  # assuming 1 to 8 CPUs
            axs[i, 0].legend()
            axs[i, 1].legend()
            axs[i, 2].legend()
            axs[i, 0].grid(True)
            axs[i, 1].grid(True)
            axs[i, 2].grid(True)
        plt.tight_layout()
        plt.savefig(f"plots/{t.lower()}_{test_name}.png")
        plt.close()


df = read_json_data(ROOT_DIR)
agg_df = aggregate_data(df)
plot(agg_df, "Server")
plot(agg_df, "Client")

# agg_df.to_csv('agg_benchmark_results.csv', index=False)
# agg_df.to_excel('agg_benchmark_results.xlsx', index=False)
