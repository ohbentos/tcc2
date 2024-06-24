# format: "query" : "name"
from functools import partial

import db.mongodb as mongodb
import db.neo4j as neo4j
import filters


def mongodb_tests():
    return {
        "graph_view": [
            mongodb.graph_view(10),
            mongodb.graph_view(100),
            mongodb.graph_view(1_000),
            mongodb.graph_view(10_000),
            mongodb.graph_view(100_000),
        ],
        "vertice_view": [
            mongodb.vertice_view(10),
            mongodb.vertice_view(100),
            mongodb.vertice_view(1_000),
            mongodb.vertice_view(10_000),
            mongodb.vertice_view(100_000),
        ],
        "edge_view": [
            mongodb.edge_view(10),
            mongodb.edge_view(100),
            mongodb.edge_view(1_000),
            mongodb.edge_view(10_000),
            mongodb.edge_view(100_000),
        ],
        "all_view": [
            mongodb.all_view(10),
            mongodb.all_view(100),
            mongodb.all_view(1_000),
            mongodb.all_view(10_000),
            mongodb.all_view(100_000),
        ],
        "get_vertice_view": [
            mongodb.get_vertice_view(10),
            mongodb.get_vertice_view(100),
            mongodb.get_vertice_view(1_000),
            mongodb.get_vertice_view(10_000),
            mongodb.get_vertice_view(100_000),
        ],
        "get_edge_view": [
            mongodb.get_edge_view(10),
            mongodb.get_edge_view(100),
            mongodb.get_edge_view(1_000),
            mongodb.get_edge_view(10_000),
            mongodb.get_edge_view(100_000),
        ],
        "list_diameters": [
            mongodb.list_diameters(),
        ],
    }


def neo4j_tests(db_name: str):
    return {
        "graph_view": [
            neo4j.graph_view(10),
            neo4j.graph_view(100),
            neo4j.graph_view(1_000),
            neo4j.graph_view(10_000),
            neo4j.graph_view(100_000),
        ],
        "vertice_view": [
            neo4j.vertice_view(10),
            neo4j.vertice_view(100),
            neo4j.vertice_view(1_000),
            neo4j.vertice_view(10_000),
            neo4j.vertice_view(100_000),
        ],
        "edge_view": [
            neo4j.edge_view(10),
            neo4j.edge_view(100),
            neo4j.edge_view(1_000),
            neo4j.edge_view(10_000),
            neo4j.edge_view(100_000),
        ],
        "all_view": (
            [
                neo4j.all_view_separated(10),
                neo4j.all_view_separated(100),
                neo4j.all_view_separated(1_000),
                neo4j.all_view_separated(10_000),
                neo4j.all_view_separated(100_000),
            ]
            if db_name == "neo4j_separated"
            else [
                neo4j.all_view_unified(10),
                neo4j.all_view_unified(100),
                neo4j.all_view_unified(1_000),
                neo4j.all_view_unified(10_000),
                neo4j.all_view_unified(100_000),
            ]
        ),
        "get_vertice_view": [
            neo4j.get_vertice_view(10),
            neo4j.get_vertice_view(100),
            neo4j.get_vertice_view(1_000),
            neo4j.get_vertice_view(10_000),
            neo4j.get_vertice_view(100_000),
        ],
        "get_edge_view": [
            neo4j.get_edge_view(10),
            neo4j.get_edge_view(100),
            neo4j.get_edge_view(1_000),
            neo4j.get_edge_view(10_000),
            neo4j.get_edge_view(100_000),
        ],
        "list_diameters": [
            {
                """
MATCH (p:Props)
WHERE p.p51> 2
WITH p.p51 AS diameter, COLLECT(p.graph_id) AS graph_ids
RETURN diameter, graph_ids  ORDER BY diameter ASC
""": None
            },
        ],
    }


postgres_tests = {
    "graph_view": [
        {"SELECT * FROM graph_view LIMIT 10": "10"},
        {"SELECT * FROM graph_view LIMIT 100": "100"},
        {"SELECT * FROM graph_view LIMIT 1000": "1000"},
        {"SELECT * FROM graph_view LIMIT 10000": "10000"},
        {"SELECT * FROM graph_view LIMIT 100000": "100000"},
    ],
    "vertice_view": [
        {"SELECT * FROM vertice_view LIMIT 10": "10"},
        {"SELECT * FROM vertice_view LIMIT 100": "100"},
        {"SELECT * FROM vertice_view LIMIT 1000": "1000"},
        {"SELECT * FROM vertice_view LIMIT 10000": "10000"},
        {"SELECT * FROM vertice_view LIMIT 100000": "100000"},
    ],
    "edge_view": [
        {"SELECT * FROM edge_view LIMIT 10": "10"},
        {"SELECT * FROM edge_view LIMIT 100": "100"},
        {"SELECT * FROM edge_view LIMIT 1000": "1000"},
        {"SELECT * FROM edge_view LIMIT 10000": "10000"},
        {"SELECT * FROM edge_view LIMIT 100000": "100000"},
    ],
    "all_view": [
        {"SELECT * FROM all_view LIMIT 10": "10"},
        {"SELECT * FROM all_view LIMIT 100": "100"},
        {"SELECT * FROM all_view LIMIT 1000": "1000"},
        {"SELECT * FROM all_view LIMIT 10000": "10000"},
        {"SELECT * FROM all_view LIMIT 100000": "100000"},
    ],
    "get_vertice_view": [
        {"SELECT * FROM get_vertice_view LIMIT 10": "10"},
        {"SELECT * FROM get_vertice_view LIMIT 100": "100"},
        {"SELECT * FROM get_vertice_view LIMIT 1000": "1000"},
        {"SELECT * FROM get_vertice_view LIMIT 10000": "10000"},
        {"SELECT * FROM get_vertice_view LIMIT 100000": "100000"},
    ],
    "get_edge_view": [
        {"SELECT * FROM get_edge_view LIMIT 10": "10"},
        {"SELECT * FROM get_edge_view LIMIT 100": "100"},
        {"SELECT * FROM get_edge_view LIMIT 1000": "1000"},
        {"SELECT * FROM get_edge_view LIMIT 10000": "10000"},
        {"SELECT * FROM get_edge_view LIMIT 100000": "100000"},
    ],
    "list_diameters": [
        {
            "SELECT p51 as diameter, array_agg(graph_id) AS graph_ids FROM graphs WHERE p51 > 2 GROUP BY p51 ORDER BY p51 ASC": None
        },
    ],
}

graphs_vertices_filtered_f1 = partial(
    filters.graphs_vertices_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5",
)
graphs_vertices_filtered_f2 = partial(
    filters.graphs_vertices_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p3 > 3",
)
graphs_vertices_filtered_f3 = partial(
    filters.graphs_vertices_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p1 > 2 AND v.p4 > 5",
)
graphs_vertices_filtered_f4 = partial(
    filters.graphs_vertices_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p1 > 2 AND v.p4 > 5 AND v.p5 > 3",
)
graphs_edges_filtered_f1 = partial(
    filters.graphs_edges_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 5",
)
graphs_edges_filtered_f2 = partial(
    filters.graphs_edges_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 5 AND e.p3 > 3",
)
graphs_edges_filtered_f3 = partial(
    filters.graphs_edges_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 5 AND e.p3 > 3 AND e.p4 > 5",
)
graphs_edges_filtered_f4 = partial(
    filters.graphs_edges_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 5 AND e.p1 > 3 AND e.p4 > 4 AND e.p5 > 3",
)
graphs_filtered_f1 = partial(
    filters.graphs_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5",
    edge_filter="e.p1 > 5",
)
graphs_filtered_f2 = partial(
    filters.graphs_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p3 > 3",
    edge_filter="e.p1 > 5 AND e.p3 > 3",
)
graphs_filtered_f3 = partial(
    filters.graphs_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p1 > 2 AND v.p4 > 5",
    edge_filter="e.p1 > 5 AND e.p1 > 2 AND e.p4 > 5",
)
graphs_filtered_f4 = partial(
    filters.graphs_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 5 AND v.p1 > 2 AND v.p4 > 5 AND v.p5 > 3",
    edge_filter="e.p1 > 5 AND e.p1 > 2 AND e.p4 > 5 AND e.p5 > 3",
)
graphs_vertices_all_filtered_f1 = partial(
    filters.graphs_vertices_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2",
)
graphs_vertices_all_filtered_f2 = partial(
    filters.graphs_vertices_all_filtered,
    graph_filter="g.p1 > 10 ",
    vertice_filter="v.p1 > 2 AND v.p3 > 3",
)
graphs_vertices_all_filtered_f3 = partial(
    filters.graphs_vertices_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2 AND v.p3 > 3 AND v.p4 > 2",
)
graphs_vertices_all_filtered_f4 = partial(
    filters.graphs_vertices_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2 AND v.p3 > 3 AND v.p4 > 2 AND v.p5 > 3",
)
graphs_edges_all_filtered_f1 = partial(
    filters.graphs_edges_all_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 2",
)
graphs_edges_all_filtered_f2 = partial(
    filters.graphs_edges_all_filtered,
    graph_filter="g.p1 > 10 ",
    edge_filter="e.p1 > 2 AND e.p3 > 3",
)
graphs_edges_all_filtered_f3 = partial(
    filters.graphs_edges_all_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 2 AND e.p3 > 3 AND e.p4 > 2",
)
graphs_edges_all_filtered_f4 = partial(
    filters.graphs_edges_all_filtered,
    graph_filter="g.p1 > 10",
    edge_filter="e.p1 > 2 AND e.p3 > 3 AND e.p4 > 2 AND e.p5 > 3",
)
graphs_all_filtered_f1 = partial(
    filters.graphs_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2.2",
    edge_filter="e.p1 > 2.2",
)
graphs_all_filtered_f2 = partial(
    filters.graphs_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2.2 AND v.p2 > 2.3",
    edge_filter="e.p1 > 2.2 AND e.p2 > 2.3",
)
graphs_all_filtered_f3 = partial(
    filters.graphs_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2.2 AND v.p2 > 2.3 AND v.p3 > 2.4",
    edge_filter="e.p1 > 2.2 AND e.p2 > 2.3 AND e.p3 > 2.4",
)
graphs_all_filtered_f4 = partial(
    filters.graphs_all_filtered,
    graph_filter="g.p1 > 10",
    vertice_filter="v.p1 > 2.2 AND v.p2 > 2.3 AND v.p3 > 2.4 AND v.p4 > 2.5",
    edge_filter="e.p1 > 2.2 AND e.p2 > 2.3 AND e.p3 > 2.4 AND e.p4 > 2.5",
)


def get_tests(db_name: str):
    global postgres_tests, neo4j_tests

    filtered_tests = {
        "graphs_vertices_filtered_f1": [
            {graphs_vertices_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_filtered_f2": [
            {graphs_vertices_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_filtered_f3": [
            {graphs_vertices_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_filtered_f4": [
            {graphs_vertices_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_filtered_f4(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_filtered_f1": [
            {graphs_edges_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_filtered_f2": [
            {graphs_edges_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_filtered_f3": [
            {graphs_edges_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_filtered_f4": [
            {graphs_edges_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f4(db_name=db_name, limit=None): None},
        ],
        "graphs_filtered_f1": [
            {graphs_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_filtered_f2": [
            {graphs_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_filtered_f3": [
            {graphs_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_filtered_f4": [
            {graphs_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f4(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_all_filtered_f1": [
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_all_filtered_f2": [
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_all_filtered_f3": [
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_vertices_all_filtered_f4": [
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_all_filtered_f1": [
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_all_filtered_f2": [
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_all_filtered_f3": [
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_edges_all_filtered_f4": [
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit=None): None},
        ],
        "graphs_all_filtered_f1": [
            {graphs_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f1(db_name=db_name, limit=None): None},
        ],
        "graphs_all_filtered_f2": [
            {graphs_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f2(db_name=db_name, limit=None): None},
        ],
        "graphs_all_filtered_f3": [
            {graphs_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f3(db_name=db_name, limit=None): None},
        ],
        "graphs_all_filtered_f4": [
            {graphs_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f4(db_name=db_name, limit=None): None},
        ],
    }

    # filtered_tests = {}

    if db_name.startswith("graph_"):
        for key, value in postgres_tests.items():
            filtered_tests[key] = value
    elif db_name.startswith("neo4j_"):
        for key, value in neo4j_tests(db_name).items():
            filtered_tests[key] = value
    elif db_name.startswith("mongo"):
        for key, value in mongodb_tests().items():
            filtered_tests[key] = value

    else:
        print("Unknown database " + db_name)
        exit(0)

    return filtered_tests
