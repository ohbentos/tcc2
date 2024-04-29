from typing import Dict

import numpy as np


def calculate_statistics(result: Dict[str, float]) -> Dict:
    stats = {}
    data = np.array([x["mem"] for x in result])  # type: ignore
    if len(data) != 0:
        mean = np.mean(data).astype(float)
        median = np.median(data).astype(float)
        variance = np.var(data).astype(float)
        min = np.min(data).astype(float)
        max = np.max(data).astype(float)
    else:
        mean = 0
        median = 0
        variance = 0
        min = 0
        max = 0

    stats["mem"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
    }

    data = np.array([x["cpu"] for x in result])  # type: ignore
    if len(data) != 0:
        mean = np.mean(data).astype(float)
        median = np.median(data).astype(float)
        variance = np.var(data).astype(float)
        min = np.min(data).astype(float)
        max = np.max(data).astype(float)
    else:
        mean = 0
        median = 0
        variance = 0
        min = 0
        max = 0

    stats["cpu"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
    }

    return stats
