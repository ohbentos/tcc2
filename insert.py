import json
import uuid

import numpy as np
from tqdm import tqdm

from db.postgres import PGDatabase
from helpers.files import count_file_lines


def main():
    # insert_data(PGDatabase(8001))
    # insert_data_edge_primary(
        # PGDatabase(8004),
        # reset=False,
    # )  # reset=True)
    pass


def insert_data(db: PGDatabase, reset=False):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt", "r")

    db.start()
    db.create_db_3_tables(reset)

    i = 0
    for graph_line in tqdm(
        grafos_file, total=count_file_lines(open("./data/grafos_10_a_20.txt", "rb"))
    ):
        i += 1
        props_line = props_file.readline()
        # while i < 1856529:
        #     props_line = props_file.readline()
        #     i += 1
        #     continue

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        if int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]
        elif int(props_id) < int(graph_id):
            props_line = props_file.readline()
            props_list = props_line.strip("\n").split("\t")
            props_id = float(props_list[0])

        props = filter_props(props_list[1:])

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
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
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
INSERT INTO edges VALUES {",".join(f"({edge})" for edge in edges_value_list)}
        """

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            ",".join(
                [
                    f"'{vertice_id}'",
                    f"'{graph_uuid}'",
                    ",".join(vertices_random_param[i]),
                ]
            )
            for i, vertice_id in enumerate(vertices_uuids)
        ]

        vertices_query = f"""
INSERT INTO vertices VALUES {",".join(f"({vertice_value})" for vertice_value in vertices_value_list)}
        """
        db.execute(f"{props_query}\n; {vertices_query}\n; {edges_query}\n;")


def filter_props(props: list[str]) -> list[str]:
    for ii, x in enumerate(props):
        if x == "NaN":
            props[ii] = "'NaN'"
        elif x == "-Inf":
            props[ii] = "'-Infinity'"
        elif x == "Inf":
            props[ii] = "'Infinity'"
    return props


def insert_data_unified(db: PGDatabase, reset=False):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt", "r")

    db.start()
    db.create_db_unified(reset)

    i = 0
    for graph_line in tqdm(
        grafos_file, total=count_file_lines(open("./data/grafos_10_a_20.txt", "rb"))
    ):
        i += 1
        props_line = props_file.readline()

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        if int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]
        elif int(props_id) < int(graph_id):
            props_line = props_file.readline()
            props_list = props_line.strip("\n").split("\t")
            props_id = float(props_list[0])

        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            ",".join(
                [
                    f"'{uuid.uuid4()}'",
                    f"'{vertices_uuids[x[0]]}'",
                    f"'{vertices_uuids[x[1]]}'",
                    ",".join(edges_random_param[i]),
                ]
            )
            for i, x in enumerate(graph_edges)
        ]

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            ",".join(
                [
                    f"'{vertice_id}'",
                    ",".join(vertices_random_param[i]),
                ]
            )
            for i, vertice_id in enumerate(vertices_uuids)
        ]

        query = f"""
INSERT INTO graphs VALUES ('{graph_uuid}',
ARRAY[{",".join([f"ROW({x})" for x in edges_value_list])}]::edge[],
ARRAY[{",".join([f"ROW({x})" for x in vertices_value_list])}]::vertice[],
{','.join(props)})
       """

        db.execute(query)


def insert_data_json(db: PGDatabase, reset=False):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt", "r")

    db.start()
    db.create_db_json(reset)

    i = 0
    for graph_line in tqdm(
        grafos_file, total=count_file_lines(open("./data/grafos_10_a_20.txt", "rb"))
    ):
        i += 1
        props_line = props_file.readline()

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        if int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]
        elif int(props_id) < int(graph_id):
            props_line = props_file.readline()
            props_list = props_line.strip("\n").split("\t")
            props_id = float(props_list[0])

        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            {
                "id": uuid.uuid4().__str__(),
                "vertice1": vertices_uuids[x[0]].__str__(),
                "vertice2": vertices_uuids[x[1]].__str__(),
                "p1": edges_random_param[i][0],
                "p2": edges_random_param[i][1],
                "p3": edges_random_param[i][2],
                "p4": edges_random_param[i][3],
                "p5": edges_random_param[i][4],
                "p6": edges_random_param[i][5],
                "p7": edges_random_param[i][6],
                "p8": edges_random_param[i][7],
                "p9": edges_random_param[i][8],
                "p10": edges_random_param[i][9],
            }
            for i, x in enumerate(graph_edges)
        ]

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            {
                "id": vertice_id.__str__(),
                "p1": vertices_random_param[i][0],
                "p2": vertices_random_param[i][1],
                "p3": vertices_random_param[i][2],
                "p4": vertices_random_param[i][3],
                "p5": vertices_random_param[i][4],
                "p6": vertices_random_param[i][5],
                "p7": vertices_random_param[i][6],
                "p8": vertices_random_param[i][7],
                "p9": vertices_random_param[i][8],
                "p10": vertices_random_param[i][9],
            }
            for i, vertice_id in enumerate(vertices_uuids)
        ]

        query = f"""
INSERT INTO graphs VALUES ('{graph_uuid}',
'{json.dumps(edges_value_list)}'::jsonb,
'{json.dumps(vertices_value_list)}'::jsonb,
{','.join(props)})
       """

        db.execute(query)


def insert_data_vertice_primary(db: PGDatabase, reset=False):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt", "r")

    db.start()
    db.create_db_vertice_primary(reset)

    i = 0
    for graph_line in tqdm(
        grafos_file, total=count_file_lines(open("./data/grafos_10_a_20.txt", "rb"))
    ):
        i += 1
        props_line = props_file.readline()

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        if int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]
        elif int(props_id) < int(graph_id):
            props_line = props_file.readline()
            props_list = props_line.strip("\n").split("\t")
            props_id = float(props_list[0])

        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            ",".join(
                [
                    f"'{uuid.uuid4()}'",
                    ",".join([f"{x}" for x in edges_random_param[i]]),
                ]
            )
            for i, _ in enumerate(graph_edges)
        ]


        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            ",".join(
                [
                    f"'{vertice_id}'",
                    f"ARRAY[ {",".join([f'ROW({x})' for x in  edges_value_list])} ]::edge[]",
                    ",".join(vertices_random_param[i]),
                ]
            )
            for i, vertice_id in enumerate(vertices_uuids)
        ]

        query = f"""
INSERT INTO graphs VALUES ('{graph_uuid}',
ARRAY[\n{",".join([f"\n  ROW({x})\n" for x in vertices_value_list])}]::vertice[],
{','.join(props)})
       """

        db.execute(query)

def insert_data_edge_primary(db: PGDatabase, reset=False):
    grafos_file = open("./data/grafos_10_a_20.txt", "r")
    props_file = open("./data/metricas.limpo.txt", "r")

    db.start()
    db.create_db_edge_primary(reset)

    i = 0
    for graph_line in tqdm(
        grafos_file, total=count_file_lines(open("./data/grafos_10_a_20.txt", "rb"))
    ):
        i += 1
        props_line = props_file.readline()

        props_list = props_line.strip("\n").split("\t")
        props_id = float(props_list[0])

        graph_list = graph_line.strip("\n").split(" ")
        graph_id = graph_list[0]

        if int(props_id) > int(graph_id):
            graph_line = grafos_file.readline()
            graph_list = graph_line.strip("\n").split(" ")
            graph_id = graph_list[0]
        elif int(props_id) < int(graph_id):
            props_line = props_file.readline()
            props_list = props_line.strip("\n").split("\t")
            props_id = float(props_list[0])

        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        vertices_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            ",".join(
                [
                    f"'{vertice_id}'",
                    ",".join(vertices_random_param[i]),
                ]
            )
            for i, vertice_id in enumerate(vertices_uuids)
        ]

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(np.float32).astype(str)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            ",".join(
                [
                    f"'{uuid.uuid4()}'",
                    f"ARRAY[ {",".join([f'ROW({x})' for x in  vertices_value_list])} ]::vertice[]",
                    ",".join([f"{x}" for x in edges_random_param[i]]),
                ]
            )
            for i, _ in enumerate(graph_edges)
        ]


        query = f"""
INSERT INTO graphs VALUES ('{graph_uuid}',
ARRAY[\n{",".join([f"\n  ROW({x})\n" for x in edges_value_list])}]::edge[],
{','.join(props)})
       """

        db.execute(query)


if __name__ == "__main__":
    main()

# 3:41:45 to insert
