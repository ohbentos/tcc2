# format: "query" : "name"
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
}


tests = {
    "graph_unified": {
        "graphs_vertices_filtered": [
            {
                filters.graphs_vertices_filtered(
                    "graph_unified", "g.p1 > 5", "v.p1 > 4", "10"
                ): "10"
            }
        ],
    }
}


# for t in tests:
#     for st in shared_tests:
#         tests[t][st] = shared_tests[st]
