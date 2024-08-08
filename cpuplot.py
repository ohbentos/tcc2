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

                        if limit == 10_000 or limit == None:
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

# Set global font sizes, increased by one unit
plt.rc('font', size=15)  # Default text size (was 14)
plt.rc('axes', titlesize=19)  # Title size (was 18)
plt.rc('axes', labelsize=17)  # X and Y label size (was 16)
plt.rc('xtick', labelsize=15)  # X tick label size (was 14)
plt.rc('ytick', labelsize=15)  # Y tick label size (was 14, now set explicitly below)
plt.rc('legend', fontsize=15)  # Legend font size (was 14)

# Plot a stacked bar plot for each query
for query_name in df_grouped["Query"].unique():
    query_data = df_grouped[df_grouped["Query"] == query_name]

    # Plotting
    fig, ax = plt.subplots(figsize=(15, 10))
    bar_width = 0.75
    # Use a darker shade of blue
    bar1 = ax.barh(
        query_data["Model Name"],
        query_data["Uso de CPU servidor"],
        bar_width,
        label="Uso de CPU servidor",
        color="#1f77b4",
    )  # Darker blue
    bar2 = ax.barh(
        query_data["Model Name"],
        query_data["Uso de CPU cliente"],
        bar_width,
        left=query_data["Uso de CPU servidor"],
        label="Uso de CPU cliente",
        color="orange",
    )

    ax.set_title(f"Uso de CPU no cliente e servidor para a consulta {query_name} (8 CPUs, limite máximo)")
    ax.set_ylabel("Modelagem")
    ax.set_xlabel("Uso de CPU (%)")
    ax.legend()

    # Increase the font size of the y-axis tick labels (model names) by 2 units
    ax.tick_params(axis='y', which='major', labelsize=17)  # previously 15 in plt.rc

    # Use tight_layout to adjust the plot to fit elements within the figure area
    plt.tight_layout()
    # Optional: Manual adjustment of subplot parameters if tight_layout is not enough
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    plt.savefig(f"./cpuplots/cpuplot_{query_name}.png", dpi=300)
    plt.close()
