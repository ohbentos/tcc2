shared_tests = {
    "get_all_graph_properties": [
        "SELECT * FROM all_view LIMIT 10",
        "SELECT * FROM all_view LIMIT 100",
        "SELECT * FROM all_view LIMIT 1000",
        "SELECT * FROM all_view LIMIT 10000",
        "SELECT * FROM all_view LIMIT 100000",
        "SELECT * FROM all_view LIMIT 1000000",
    ],
    "get_all_graph_vertices": [
        "SELECT * FROM vertice_view LIMIT 10",
        "SELECT * FROM vertice_view LIMIT 100",
        "SELECT * FROM vertice_view LIMIT 1000",
        "SELECT * FROM vertice_view LIMIT 10000",
        "SELECT * FROM vertice_view LIMIT 100000",
        "SELECT * FROM vertice_view LIMIT 1000000",
    ],
    "get_all_graph_edges": [
        "SELECT * FROM edge_view LIMIT 10",
        "SELECT * FROM edge_view LIMIT 100",
        "SELECT * FROM edge_view LIMIT 1000",
        "SELECT * FROM edge_view LIMIT 10000",
        "SELECT * FROM edge_view LIMIT 100000",
        "SELECT * FROM edge_view LIMIT 1000000",
    ],
    "get_all_graph_information": [
        "SELECT * FROM graph_view LIMIT 10",
        "SELECT * FROM graph_view LIMIT 100",
        "SELECT * FROM graph_view LIMIT 1000",
        "SELECT * FROM graph_view LIMIT 10000",
        "SELECT * FROM graph_view LIMIT 100000",
        "SELECT * FROM graph_view LIMIT 1000000",
    ],
    "get_all_vertices_information": [
        "SELECT * FROM get_vertice_view LIMIT 10",
        "SELECT * FROM get_vertice_view LIMIT 100",
        "SELECT * FROM get_vertice_view LIMIT 1000",
        "SELECT * FROM get_vertice_view LIMIT 10000",
        "SELECT * FROM get_vertice_view LIMIT 100000",
        "SELECT * FROM get_vertice_view LIMIT 1000000",
    ],
    "get_all_edges_information": [
        "SELECT * FROM get_edge_view LIMIT 10",
        "SELECT * FROM get_edge_view LIMIT 100",
        "SELECT * FROM get_edge_view LIMIT 1000",
        "SELECT * FROM get_edge_view LIMIT 10000",
        "SELECT * FROM get_edge_view LIMIT 100000",
        "SELECT * FROM get_edge_view LIMIT 1000000",
    ]
}

tests = {
    "graph_unified": {
    },
    "graph_unified": {
    }
}


for t in tests:
    for st in shared_tests:
        tests[t][st] = shared_tests[st]
