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
        perc_99 = np.percentile(data, 99).astype(float)
        perc_95 = np.percentile(data, 95).astype(float)
        perc_90 = np.percentile(data, 90).astype(float)
        perc_75 = np.percentile(data, 75).astype(float)
        perc_50 = np.percentile(data, 50).astype(float)
        dp = np.std(data).astype(float)
    else:
        mean = 0
        median = 0
        variance = 0
        min = 0
        max = 0
        perc_99 = 0
        perc_95 = 0
        perc_90 = 0
        perc_75 = 0
        perc_50 = 0
        dp = 0

    stats["mem"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
        "std_deviation": dp,
        "perc_99": perc_99,
        "perc_95": perc_95,
        "perc_90": perc_90,
        "perc_75": perc_75,
        "perc_50": perc_50,
    }

    data = np.array([x["cpu"] for x in result])  # type: ignore
    if len(data) != 0:
        mean = np.mean(data).astype(float)
        median = np.median(data).astype(float)
        variance = np.var(data).astype(float)
        min = np.min(data).astype(float)
        max = np.max(data).astype(float)
        perc_99 = np.percentile(data, 99).astype(float)
        perc_95 = np.percentile(data, 95).astype(float)
        perc_90 = np.percentile(data, 90).astype(float)
        perc_75 = np.percentile(data, 75).astype(float)
        perc_50 = np.percentile(data, 50).astype(float)
        dp = np.std(data).astype(float)
    else:
        mean = 0
        median = 0
        variance = 0
        min = 0
        max = 0
        perc_99 = 0
        perc_95 = 0
        perc_90 = 0
        perc_75 = 0
        perc_50 = 0
        dp = 0

    stats["cpu"] = {
        "mean": mean,
        "median": median,
        "variance": variance,
        "min": min,
        "max": max,
        "samples": len(data),
        "std_deviation": dp,
        "perc_99": perc_99,
        "perc_95": perc_95,
        "perc_90": perc_90,
        "perc_75": perc_75,
        "perc_50": perc_50,
    }

    return stats
