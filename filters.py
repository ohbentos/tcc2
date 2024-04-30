def graphs_vertices_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_vertices_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_edges_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_edges_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, edge_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_vertices_all_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_vertices_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{limit}}", limit)
        return query

def graphs_edges_all_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_edges_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query

def graphs_all_filtered(
    db_name: str, graph_filter: str, vertice_filter: str,edge_filter: str, limit: str
) -> str:
    with open(f"./filter_queries/{db_name}/graphs_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query
