import json
import os

import matplotlib.pyplot as plt
import pandas as pd

# Define the base directory
base_dir = "results"

# Initialize an empty list to store the data
data = []

# Traverse the directory structure
for model_name in os.listdir(base_dir):
    model_dir = os.path.join(base_dir, model_name)
    if os.path.isdir(model_dir):
        cpu_dir = os.path.join(model_dir, "8")  # Choose the directory for 8 CPUs
        if os.path.isdir(cpu_dir):
            for json_file in os.listdir(cpu_dir):
                if json_file.endswith(".json"):
                    json_path = os.path.join(cpu_dir, json_file)
                    with open(json_path, "r") as f:
                        content = json.load(f)

                        # Extracting query info: Assuming limit is encoded in the filename appropriately
                        try:
                            limit = int(json_file.split("-")[-1].replace(".json", ""))
                        except ValueError:  # handle 'None' case
                            limit = None

                        if (
                            limit == 10_000 or limit == None
                        ):  # Use the actual limit you want, e.g., 1000
                            # Extract the cpu mean usage from both server and client stats
                            server_cpu_mean = content["server"]["stats"]["cpu"]["mean"]
                            client_cpu_mean = content["client"]["stats"]["cpu"]["mean"]
                            query_name = content["run_config"]["test_name"]

                            # Append the extracted info to the data list
                            data.append(
                                {
                                    "Model Name": model_name,
                                    "Query": query_name,
                                    "Uso de CPU servidor": server_cpu_mean,
                                    "Uso de CPU cliente": client_cpu_mean,
                                }
                            )

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Group by 'Model Name' and 'Query' and calculate the mean of CPU usages
df["Model Name"] = df["Model Name"].str.replace("^graph_", "postgres_", regex=True)
df_grouped = df.groupby(["Model Name", "Query"]).mean().reset_index()

# Plot a stacked bar plot for each query
for query_name in df_grouped["Query"].unique():
    query_data = df_grouped[df_grouped["Query"] == query_name]

    # Plotting
    plt.figure(figsize=(15, 10))
    bar_width = 0.75
    # Use a darker shade of blue
    bar1 = plt.barh(
        query_data["Model Name"],
        query_data["Uso de CPU servidor"],
        bar_width,
        label="Uso de CPU servidor",
        color="#1f77b4",
    )  # Darker blue
    bar2 = plt.barh(
        query_data["Model Name"],
        query_data["Uso de CPU cliente"],
        bar_width,
        left=query_data["Uso de CPU servidor"],
        label="Uso de CPU cliente",
        color="orange",
    )

    plt.title(
        f"Uso de CPU no cliente e servidor para a consulta {query_name} (8 CPUs, limite máximo)"
    )
    plt.ylabel("Modelagm")
    plt.xlabel("Uso de CPU (%)")
    plt.legend()
    plt.savefig(f"./cpuplots/cpuplot_{query_name}.png", dpi=300)
    plt.close()
