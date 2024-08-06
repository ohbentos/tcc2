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
                            limit == 10000
                        ):  # Replace max_limit with the actual max limit you want
                            # Extract the cpu mean from the server stats for this particular configuration
                            cpu_mean = content["server"]["stats"]["cpu"]["mean"]
                            query_name = content["run_config"]["test_name"]

                            # Append the extracted info to the data list
                            data.append(
                                {
                                    "Model Name": model_name,
                                    "Query": query_name,
                                    "CPU Mean": cpu_mean,
                                }
                            )

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Set up the plot using seaborn
plt.figure(figsize=(15, 10))
sns.boxplot(x="Model Name", y="CPU Mean", hue="Query", data=df)
plt.title("Boxplot of CPU mean for different queries and models (8 CPUs, max limit)")
plt.xlabel("Database model")
plt.ylabel("CPU Mean Usage")
plt.xticks(rotation=45)
plt.legend(title="Query")
plt.show()
