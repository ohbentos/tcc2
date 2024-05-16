from io import BufferedReader, TextIOWrapper


def count_file_lines(f: TextIOWrapper | BufferedReader) -> int:
    total = sum(1 for _ in f)
    f.close()
    return total


def minimum_file_lines(
    f1: TextIOWrapper | BufferedReader, f2: TextIOWrapper | BufferedReader
) -> int:
    total_f1 = sum(1 for _ in f1)
    total_f2 = sum(1 for _ in f2)
    f1.close()
    f2.close()
    return min(total_f1, total_f2)
