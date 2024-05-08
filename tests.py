# format: "query" : "name"
from functools import partial

import filters

shared_tests = {
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
    global shared_tests

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
            {graphs_edges_filtered_f1(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_filtered_f2": [
            {graphs_edges_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f2(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_filtered_f3": [
            {graphs_edges_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f3(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_filtered_f4": [
            {graphs_edges_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_edges_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_filtered_f4(db_name=db_name, limit=None):None},
        ],
        "graphs_filtered_f1": [
            {graphs_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f1(db_name=db_name, limit=None):None},
        ],
        "graphs_filtered_f2": [
            {graphs_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f2(db_name=db_name, limit=None):None},
        ],
        "graphs_filtered_f3": [
            {graphs_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f3(db_name=db_name, limit=None):None},
        ],
        "graphs_filtered_f4": [
            {graphs_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_filtered_f4(db_name=db_name, limit=None):None},
        ],
        "graphs_vertices_all_filtered_f1": [
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f1(db_name=db_name, limit=None):None},
        ],
        "graphs_vertices_all_filtered_f2": [
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f2(db_name=db_name, limit=None):None},
        ],
        "graphs_vertices_all_filtered_f3": [
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f3(db_name=db_name, limit=None):None},
        ],
        "graphs_vertices_all_filtered_f4": [
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_vertices_all_filtered_f4(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_all_filtered_f1": [
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f1(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_all_filtered_f2": [
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f2(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_all_filtered_f3": [
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f3(db_name=db_name, limit=None):None},
        ],
        "graphs_edges_all_filtered_f4": [
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_edges_all_filtered_f4(db_name=db_name, limit=None):None},
        ],
        "graphs_all_filtered_f1": [
            {graphs_all_filtered_f1(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f1(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f1(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f1(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f1(db_name=db_name, limit=None):None},
        ],
        "graphs_all_filtered_f2": [
            {graphs_all_filtered_f2(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f2(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f2(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f2(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f2(db_name=db_name, limit=None):None},
        ],
        "graphs_all_filtered_f3": [
            {graphs_all_filtered_f3(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f3(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f3(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f3(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f3(db_name=db_name, limit=None):None},
        ],
        "graphs_all_filtered_f4": [
            {graphs_all_filtered_f4(db_name=db_name, limit="1"): "1"},
            {graphs_all_filtered_f4(db_name=db_name, limit="10"): "10"},
            {graphs_all_filtered_f4(db_name=db_name, limit="100"): "100"},
            {graphs_all_filtered_f4(db_name=db_name, limit="1000"): "1000"},
            {graphs_all_filtered_f4(db_name=db_name, limit=None):None},
        ],
    }
    # shared_tests = {}

    for key, value in filtered_tests.items():
        shared_tests[key] = value

    return shared_tests
