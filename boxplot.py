<<<<<<< HEAD
import json
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Define the base directory
base_dir = "results"

# Initialize an empty list to store the data
data = []

# Traverse the directory structure
for model_name in os.listdir(base_dir):
    model_dir = os.path.join(base_dir, model_name)
    if os.path.isdir(model_dir):
        for cpu_count in range(1, 9):  # Iterate over CPU counts 1 to 8
            cpu_dir = os.path.join(model_dir, str(cpu_count))
            if os.path.isdir(cpu_dir):
                for json_file in os.listdir(cpu_dir):
                    if json_file.endswith(".json"):
                        json_path = os.path.join(cpu_dir, json_file)
                        with open(json_path, "r") as f:
                            content = json.load(f)
                            # Extract the execution time from the JSON content
                            execution_time = content["time"]
                            query_name = content["run_config"]["test_name"]

                            # Append the extracted info to the data list
                            data.append(
                                {
                                    "Model Name": model_name,
                                    "Query": query_name,
                                    "Execution Time": execution_time,
                                }
                            )

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)
df["Model Name"] = df["Model Name"].str.replace("^graph_", "postgres_", regex=True)

# Calculate the median execution time for each model
median_times = df.groupby("Model Name")["Execution Time"].median().reset_index()

# Print the median execution times
for index, row in median_times.iterrows():
    print(f"Model: {row['Model Name']}, Median Execution Time: {row['Execution Time']} seconds")

# Create the custom properties for the boxplot
boxprops = dict(facecolor="none", edgecolor="black")
whiskerprops = dict(color="black")
capprops = dict(color="black")
medianprops = dict(color="red")

# Plot a boxplot for each model, combining all queries, with custom colors
plt.figure(figsize=(15, 15))  # Increase the second value to make the plot taller
sns.boxplot(
    x="Model Name",
    y="Execution Time",
    data=df,
    showfliers=False,
    boxprops=boxprops,
    whiskerprops=whiskerprops,
    capprops=capprops,
    medianprops=medianprops,
)
plt.title("Boxplot do tempo de execução de todas as consultas por modelagem")
plt.xlabel("Modelagem")
plt.ylabel("Tempo de execução (s)")
plt.xticks(rotation=45)
plt.savefig("boxplot.png", dpi=300)
# plt.show()
