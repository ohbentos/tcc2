from collections.abc import Iterable


def count_file_lines(f: Iterable) -> int:
    return sum(1 for _ in f)
