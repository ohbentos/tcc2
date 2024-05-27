import json
import uuid

import numpy as np
from neo4j import GraphDatabase
from tqdm import tqdm

from db.mongodb import MongoDatabase
from db.neo4j import (AUTH_NEO4J, create_edges, create_props,
                      create_props_link, create_vertices, run_neo4j_indexes)
from db.postgres import PGDatabase
from helpers.files import minimum_file_lines


class GrafoFile:
    def __init__(self, grafos_file: str, props_file: str):
        self.grafos_file = open(grafos_file, "r")
        self.props_file = open(props_file, "r")
        self.total_lines = minimum_file_lines(open(grafos_file, "rb"),open(props_file, "rb"))
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.total_lines

    def __next__(self):
        if self.index < self.total_lines:
            graph_line = self.grafos_file.readline()
            if not graph_line:
                raise StopIteration
            self.index += 1
            props_line = self.props_file.readline()
            if not props_line:
                raise StopIteration

            props_list = props_line.strip("\n").split("\t")
            graph_list = graph_line.strip("\n").split(" ")

            props_id = float(props_list[0])
            graph_id = float(graph_list[0])

            while props_id != graph_id:
                if props_id > graph_id:
                    graph_line = self.grafos_file.readline()
                    if not graph_line:
                        raise StopIteration
                    self.index += 1
                    graph_list = graph_line.strip("\n").split(" ")
                    graph_id = float(graph_list[0])
                elif props_id < graph_id:
                    props_line = self.props_file.readline()
                    if not props_line:
                        raise StopIteration
                    props_list = props_line.strip("\n").split("\t")
                    props_id = float(props_list[0])

            return graph_list, props_list

        self.grafos_file.close()
        self.props_file.close()
        raise StopIteration


def main():
    # grafos = GrafoFile("./data/grafos_10_a_20.txt", "./data/metricas.limpo.txt")
    # insert_data_neo4j_unified(3000, grafos)
    pass

def create_random_dict(size: int) -> dict[str, float]:
    numbers = np.random.uniform(low=0.0, high=10, size=size).astype(np.float32)
    return  {f"p{i+1}": x for i,x in  enumerate(numbers) }


def insert_data_mongodb_unified(db: int, grafos: GrafoFile, reset=False):
    client = MongoDatabase(db).start()

    for graph_list, props_list in tqdm(grafos):
        props = props_list[1:]

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

        graph_edges = graph_list[3:]
        graph_edges = [
            (int(graph_list[i]), int(graph_list[i + 1]))
            for i in range(3, len(graph_list), 2)
        ]

        graph_uuid = uuid.uuid4()

        vertices_uuids = [uuid.uuid4() for _ in range(0, graph_n_vertices)]

        edges_random_param = [
            np.random.uniform(low=0.0, high=10, size=10).astype(float)
            for _ in range(0, len(graph_edges))
        ]

        edges_value_list = [
            {
                "graph_id": graph_uuid.__str__(),
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
            np.random.uniform(low=0.0, high=10, size=10).astype(float)
            for _ in range(0, len(vertices_uuids))
        ]

        vertices_value_list = [
            {
                "graph_id": graph_uuid.__str__(),
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

        metricas : dict[str,float | str | list] = {f"p{i+1}": float(x) for i, x in enumerate(props)}
        metricas["graph_id"] = graph_uuid.__str__()
        metricas["vertices"] = vertices_value_list
        metricas["edges"] = edges_value_list
        metricas["vertices_count"] = len(vertices_value_list)
        metricas["edges_count"] = len(edges_value_list)

        client.insert_one(metricas)

def insert_data_neo4j_separated(db: int, grafos: GrafoFile, reset=False):
    insert_data_neo4j_unified(db, grafos, reset,unified=False)

def insert_data_neo4j_unified(db: int, grafos: GrafoFile, reset=False,unified=True):
    with GraphDatabase.driver(f"neo4j://localhost:{db}", auth=AUTH_NEO4J) as driver:
        with driver.session() as session:
            if reset:
                session.run("""
CALL apoc.periodic.iterate(
  'MATCH (g) RETURN g',
  'DEATCH DELETE g',
  {batchSize: 1000, parallel: true}
)
YIELD batches, total
RETURN batches, total
""")
                session.run("""
CALL apoc.periodic.iterate(
  'MATCH ()-[g]-() RETURN g',
  'DEATCH DELETE g',
  {batchSize: 1000, parallel: true}
)
YIELD batches, total
RETURN batches, total
""")
            run_neo4j_indexes(session)
            for (graph_list,props_list) in tqdm(grafos):

                props = props_list[1:]

                graph_n_vertices = int(graph_list[1])

                edge_list = [
                    (int(graph_list[i]), int(graph_list[i + 1]))
                    for i in range(3, len(graph_list), 2)
                ]

                metricas: dict[str,float|str] = {f"p{i+1}": float(x) for i,x in enumerate(props)}

                ids_vertices = [uuid.uuid4().__str__() for _ in range(graph_n_vertices)]

                graph_id = uuid.uuid4().__str__()

                edges = [ 
                    {
                        "graph_id": graph_id,
                        "id": uuid.uuid4().__str__(),
                        "id1": ids_vertices[int(e1)],
                        "id2": ids_vertices[int(e2)],
                        "properties": create_random_dict(10),
                    } for e1, e2 in edge_list
                ]
                vertices = [
                        {
                            "id": ids_vertices[i],
                            "graph_id": graph_id,
                            "properties": create_random_dict(10),
                        } for i in range(graph_n_vertices)
                ]

                session.execute_write(create_props, graph_id, uuid.uuid4().__str__(), metricas)
                session.execute_write(create_vertices, {"vertices":vertices})
                if unified:
                    session.execute_write(create_props_link, ids_vertices, graph_id)
                session.execute_write(create_edges, {"edges":edges})



def insert_data_three(db: PGDatabase, grafos: GrafoFile, reset=False):
    db.start()
    db.create_db_three(reset)

    for (graph_list,props_list) in tqdm(grafos):
        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

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

def filter_props_np(props: list[str]) -> list[str]:
    for ii, x in enumerate(props):
        if x == "NaN":
            props[ii] = np.NaN #type: ignore
        elif x == "-Inf":
            props[ii] = -np.Infinity #type: ignore
        elif x == "Inf":
            props[ii] = np.Infinity #type: ignore
    return props


def insert_data_unified(db: PGDatabase, grafos :GrafoFile, reset=False):
    db.start()
    db.create_db_unified(reset)

    # i = 0
    for (graph_list,props_list) in tqdm(grafos):
        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

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


def insert_data_json(db: PGDatabase, grafos: GrafoFile, reset=False):
    db.start()
    db.create_db_json(reset)

    # i = 0
    for (graph_list,props_list) in tqdm(grafos):
        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

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


def insert_data_vertice_primary(db: PGDatabase, grafos: GrafoFile, reset=False):
    db.start()
    db.create_db_vertice_primary(reset)

    # i = 0
    for (graph_list,props_list) in tqdm(grafos):
        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

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

def insert_data_edge_primary(db: PGDatabase, grafos: GrafoFile, reset=False):
    db.start()
    db.create_db_edge_primary(reset)

    for (graph_list,props_list) in tqdm(grafos):
        props = filter_props(props_list[1:])

        graph_n_vertices = int(graph_list[1])
        # graph_comp_onda = graph_list[2]

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
