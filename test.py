import uuid

import numpy as np
from tqdm import tqdm

from db.postgres import PGDatabase
from helpers.files import count_file_lines


def main():
    test_file_lines(PGDatabase(8000))


def test_how_many_props():
    props = open("./data/metricas.limpo.txt")

    # all lines have 318 props!
    i = 0
    expected_props = 318
    while line := props.readline():
        i += 1
        lista_props = line.split("\t")
        n_props = len(lista_props)

        if n_props != expected_props:
            print(f"line {i} does not have {expected_props} props")


def test_file_lines(db: PGDatabase):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt")

    num_lines = 0
    with open("./data/grafos_10_a_20.txt", "rb") as f:
        num_lines = count_file_lines(f)

    db.start()
    db.create_db(False)

    i = 0
    for graph_line in tqdm(grafos_file, total=num_lines):
        i += 1
        props_line = props_file.readline()

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        while int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]

        props = props_list[1:]
        props = [
            "NULL" if (x == "NaN" or x == "Inf" or x == "-Inf") else x for x in props
        ]

        graph_n_vertices = int(graph_list[1])
        graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        props_query = f"""
INSERT INTO props VALUES ('{graph_uuid}',{' , '.join(props)})
        """

        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(str)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            ",".join(
                [
                    f"'{uuid.uuid4()}'",
                    f"'{graph_uuid}'",
                    f"'{vertices_uuids[x[0]]}'",
                    f"'{vertices_uuids[x[1]]}'",
                    ",".join(edges_random_param[i]),
                ]
            )
            for i, x in enumerate(graph_edges)
        ]
        edges_query = f"""
INSERT INTO edges VALUES {",".join(f"({x})" for x in edges_value_list)}
        """

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            ",".join([f"'{x}'", f"'{graph_uuid}'", ",".join(vertices_random_param[i])])
            for i, x in enumerate(vertices_uuids)
        ]

        vertices_query = f"""
INSERT INTO vertices VALUES {",".join(f"({x})" for x in vertices_value_list)}
        """
        db.execute(f"{props_query}\n; {vertices_query}\n; {edges_query}\n;")


if __name__ == "__main__":
    main()
