from io import BufferedReader


def count_file_lines(f: BufferedReader) -> int:
    return sum(1 for _ in f)
