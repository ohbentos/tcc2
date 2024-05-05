import os
import json
import pandas as pd

ROOT_DIR = 'results'

def read_json_data(root_dir:str) -> pd.DataFrame:
    data = []
    
    # Traverse through the directory structure
    for db_name in os.listdir(root_dir):
        db_path = os.path.join(root_dir, db_name)
        if os.path.isdir(db_path):
            for cpu_count in os.listdir(db_path):
                cpu_path = os.path.join(db_path, cpu_count)
                if os.path.isdir(cpu_path):
                    for file_name in os.listdir(cpu_path):
                        if file_name.endswith('.json'):
                            file_path = os.path.join(cpu_path, file_name)
                            with open(file_path, 'r') as file:
                                json_data = json.load(file)
                                # Extract required data
                                run_config = json_data.get("run_config")
                                test_name = run_config.get("test_name")
                                run_number = run_config.get("run_number")
                                test_id = run_config.get("test_id")

                                server_stats = json_data.get("server", {}).get("stats", {})
                                client_stats = json_data.get("client", {}).get("stats", {})

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
                                data.append({
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
                                    "Server Memory Std": server_mem["std_deviation"],

                                    

                                    "Client CPU Mean": client_cpu["mean"],
                                    "Client CPU Median": client_cpu["median"],
                                    "Client CPU Max": client_cpu["max"],
                                    "Client CPU Min": client_cpu["min"],
                                    "Client CPU Std": client_cpu["std_deviation"],

                                    "Client Memory Mean": client_mem["mean"],
                                    "Client Memory Median": client_mem["median"],
                                    "Client Memory Max": client_mem["max"],
                                    "Client Memory Min": client_mem["min"],
                                    "Client Memory Std": client_mem["std_deviation"],
                                })
    
    return pd.DataFrame(data)

def aggregate_data(df : pd.DataFrame):
    # Group by Database, CPUs, and Test Name, then calculate mean
    agg_df = df.groupby(['Test Name', "Limit",'Database', 'CPUs' ]).mean().reset_index().sort_values(by=['Test Name','CPUs', 'Limit'])
    
    return agg_df

df = read_json_data(ROOT_DIR)
agg_df = aggregate_data(df)
print(agg_df)

# agg_df.to_csv('agg_benchmark_results.csv', index=False)
agg_df.to_excel('agg_benchmark_results.xlsx', index=False)
