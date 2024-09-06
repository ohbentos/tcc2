import json
import math
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.lines import Line2D
import matplotlib.patheffects as PathEffects

# Load the data
f = open("vertice_edge_diameter.json")
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
        aggregated_data[number_of_nodes][diameter].append((number_of_edges, count))

# Determine the global range of number_of_edges
all_edges = [entry["number_of_edges"] for entry in data]
global_min_edges = min(all_edges)
global_max_edges = max(all_edges)

# Create a consistent color map for diameters
unique_diameters = sorted(
    set([dist["diameter"] for entry in data for dist in entry["diameter_distribution"]])
)
color_map = plt.get_cmap("tab10", len(unique_diameters))
color_dict = {diameter: color_map(i) for i, diameter in enumerate(unique_diameters)}

# Determine the number of subplots
num_subplots = len(aggregated_data)
cols = 2  # Number of columns in the subplot grid
rows = math.ceil(num_subplots / cols)

# Variables to control the size of subplots
horizontal_size = 12  # Width of each subplot
vertical_size = 6  # Height of each subplot

# Increase the figure size to make subplots larger
fig, axes = plt.subplots(rows, cols, figsize=(horizontal_size * cols, vertical_size * rows), squeeze=False)

main_handles = [
    Line2D(
        [0],
        [0],
        color=color_dict[diameter],
        lw=1,  # Thinner line for the legend
        marker="o",
        markersize=4,  # Smaller circles for the legend
        label=f"Diâmetro: {diameter}",
    )
    for diameter in unique_diameters
]

# Plot each number_of_nodes in a subplot
comb = len(aggregated_data.items())
for i, (number_of_nodes, diameter_data) in enumerate(aggregated_data.items()):
    row = i // cols
    col = i % cols
    ax = axes[row, col]

    for diameter in unique_diameters:
        if diameter in diameter_data:
            values = diameter_data[diameter]
            counts = [val[1] for val in values]
            # Only plot the line if counts are not all zero
            if any(counts):
                line, = ax.plot(
                    [val[0] for val in values],
                    counts,
                    label=f"Diâmetro: {diameter}",
                    color=color_dict[diameter],
                    lw=1,  # Thinner line
                    marker="o",
                    markersize=4,  # Smaller circles
                )
                # Annotate each point with the count value
                for val in values:
                    ax.annotate(
                        str(val[1]),
                        (val[0], val[1]),
                        textcoords="offset points",
                        xytext=(0, 5),
                        ha='center',
                        color=color_dict[diameter]
                    )

    ax.set_title(f"Número de nós: {number_of_nodes}", fontsize=12)
    ax.set_xlabel("Número de arestas", fontsize=10)
    ax.set_ylabel("Quantidade de grafos", fontsize=10)
    ax.set_xlim(global_min_edges, global_max_edges)
    ax.set_xticks(range(global_min_edges, global_max_edges + 1))
    ax.tick_params(axis="x", rotation=45)

    # Add all diameters to legend, highlight zero-count diameters in red
    legend_labels = [
        f"Diâmetro: {diameter}"
        for diameter in unique_diameters
    ]
    legend_handles = [
        Line2D(
            [0],
            [0],
            color=color_dict[diameter],
            lw=1,  # Thinner line for the legend
            marker="o",
            markersize=2  # Smaller circles for the legend
        )
        for diameter in unique_diameters
    ]
    
    leg = ax.legend(handles=legend_handles, labels=legend_labels, loc="upper center", ncol=4)
    
    # Change the color of the text in the legend
    for idx, text in enumerate(leg.get_texts()):
        if not any([val[1] for val in diameter_data.get(unique_diameters[idx], [])]):
            text.set_color('red')
            # Adding path effect to enhance red color visibility
            text.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='none')])

# Hide any empty subplots
for j in range(comb, rows * cols):
    fig.delaxes(axes[j // cols, j % cols])

# Create a single legend for all subplots
fig.legend(handles=main_handles, loc="upper center", ncol=4, title="Legenda")

# Adjust layout
plt.subplots_adjust(hspace=0.9, wspace=0.9, top=0.9)
fig.suptitle("Distribuição do número de nós e arestas", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # type: ignore
plt.savefig("diameter_distribution.png", dpi=400)
