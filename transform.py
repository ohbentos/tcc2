import re


def transform_query(query: str, letter: str):
    pattern = letter + r"\.p(\d{1,2})"
    return re.sub(pattern, f"({letter}" + r"->>'p\1')::real", query)


# print(transform_query("e.p1 > 2.2 AND e.p2 > 2.3 AND e.p3 > 2.4 AND e.p4 > 2.5", "e"))
