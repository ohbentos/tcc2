import json
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.lines import Line2D

f = open("node_diameter.json")
data = json.load(f)
