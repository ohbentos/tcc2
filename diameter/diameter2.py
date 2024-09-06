import json
import math
import matplotlib.pyplot as plt
from collections import defaultdict

# Load the data
with open("vertice_edge_diameter.json") as f:
    data = json.load(f)

# Aggregate the data
aggregated_data = defaultdict(lambda: defaultdict(list))

for entry in data:
    number_of_nodes = entry["number_of_vertices"]
    number_of_edges = entry["number_of_edges"]
    diameter_distribution = entry["diameter_distribution"]

    for dist in diameter_distribution:
        diameter = dist["diameter"]
        count = dist["count"]
        aggregated_data[number_of_nodes][number_of_edges].append((diameter, count))

# Determine the global range of number_of_edges and number_of_diameters
all_edges = [entry["number_of_edges"] for entry in data]
global_min_edges = min(all_edges)
global_max_edges = max(all_edges)

all_diameters = [
    dist["diameter"] for entry in data for dist in entry["diameter_distribution"]
]
global_min_diameter = min(all_diameters)
global_max_diameter = max(all_diameters)

# Determine the number of subplots
num_subplots = len(aggregated_data)
cols = 2  # Number of columns in the subplot grid
rows = math.ceil(num_subplots / cols)

# Variables to control the size of subplots
horizontal_size = 12 * 1.5  # 1.5 times the current width of each subplot
vertical_size = 6  # Height of each subplot

# Increase the figure size to make subplots larger
fig, axes = plt.subplots(
    rows, cols, figsize=(horizontal_size * cols, vertical_size * rows), squeeze=False
)

# Plot each number_of_nodes in a subplot
for i, (number_of_nodes, edge_data) in enumerate(aggregated_data.items()):
    row = i // cols
    col = i % cols
    ax = axes[row, col]

    for number_of_edges, diameters in edge_data.items():
        for diameter, count in diameters:
            # Plot the dot
            ax.scatter(
                number_of_edges, diameter, s=50, color="red", zorder=5
            )  # Add zorder to ensure markers appear on top

            # Annotate each point with the count value
            ax.annotate(
                str(count),
                (number_of_edges, diameter),
                textcoords="offset points",
                xytext=(0, 5),  # Move the text above the circle
                ha="center",
                color="red",
                fontweight="bold",  # Make the font bold
                zorder=5,  # Ensure annotation appears on top
            )

    ax.set_title(f"Número de nós: {number_of_nodes}", fontsize=12)
    ax.set_xlabel("Número de arestas", fontsize=10)
    ax.set_ylabel("Diâmetro", fontsize=10)
    ax.set_xlim(global_min_edges - 0.5, global_max_edges + 0.5)
    ax.set_ylim(global_min_diameter - 0.5, global_max_diameter + 0.5)
    ax.set_xticks(
        range(global_min_edges, global_max_edges + 1)
    )  # Set all integer values for x-axis
    ax.set_yticks(
        range(global_min_diameter - 1, global_max_diameter + 1)
    )  # Set all integer values for y-axis
    ax.grid(True)  # Enable grid

# Hide any empty subplots
for j in range(len(aggregated_data), rows * cols):
    fig.delaxes(axes[j // cols, j % cols])

# Adjust layout
plt.subplots_adjust(
    hspace=0.5, wspace=0.3, top=0.9
)  # Adjust hspace and wspace as needed
fig.suptitle("Distribuição dos diâmetros por número de arestas", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # type: ignore
plt.savefig("diameter_distribution.png", dpi=300)
plt.savefig("diameter_distribution.svg")
