from transform import transform_query


def gen_file_name(
    db_name: str, cpu_count: int, run: int, query_id: int, test_name: str
):
    return (
        f"./results/{db_name}/{cpu_count}/{run}_{query_id}_{test_name}-{query_id}.json"
    )


def graphs_vertices_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, limit: str
) -> str:
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
    with open(f"./filter_queries/{db_name}/graphs_vertices_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_edges_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str
) -> str:
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_edges_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, edge_filter: str, limit: str
) -> str:
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
        vertice_filter = transform_query(vertice_filter, "v")
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
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
    with open(f"./filter_queries/{db_name}/graphs_vertices_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_edges_all_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str
) -> str:
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_edges_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query


def graphs_all_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, edge_filter: str, limit: str
) -> str:
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_all_filtered.sql") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        query = query.replace("{{limit}}", limit)
        return query
