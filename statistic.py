from typing import Dict, TypedDict

import numpy as np


class Result(TypedDict):
    mem: float
    cpu: float


def calculate_statistics(result: Dict[str, float]) -> Dict:
    stats = {}
    data = np.array([x["mem"] for x in result])  # type: ignore
    mean = np.mean(data).astype(float)
    median = np.median(data).astype(float)
    variance = np.var(data).astype(float)
    min = np.min(data).astype(float)
    max = np.max(data).astype(float)

    stats["mem"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
    }

    data = np.array([x["cpu"] for x in result])  # type: ignore
    mean = np.mean(data).astype(float)
    median = np.median(data).astype(float)
    variance = np.var(data).astype(float)
    min = np.min(data).astype(float)
    max = np.max(data).astype(float)

    stats["cpu"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
    }

    return stats
