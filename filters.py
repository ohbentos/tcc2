from db.mongodb import all_mongodb_filter,mongodb_filter
from transform import transform_query


def graphs_vertices_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, limit: str | None
) -> str:
    if db_name.startswith("mongo"):
        return mongodb_filter(
            graph_filter=graph_filter, vertice_filter=vertice_filter, edge_filter=None
        )
    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
    with open(f"./filter_queries/{db_name}/graphs_vertices_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def graphs_edges_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str | None
) -> str:
    if db_name.startswith("mongo"):
        return mongodb_filter(
            graph_filter=graph_filter, vertice_filter=None, edge_filter=edge_filter
        )
    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_edges_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def graphs_filtered(
    db_name: str,
    graph_filter: str,
    vertice_filter: str,
    edge_filter: str,
    limit: str | None,
) -> str:
    if db_name.startswith("mongo"):
        return mongodb_filter(
            graph_filter=graph_filter, vertice_filter=vertice_filter, edge_filter=None
        )
    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
        vertice_filter = transform_query(vertice_filter, "v")
    with open(f"./filter_queries/{db_name}/graphs_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def graphs_vertices_all_filtered(
    db_name: str, graph_filter: str, vertice_filter: str, limit: str | None
) -> str:
    if db_name.startswith("mongo"):
        return all_mongodb_filter(
            graph_filter=graph_filter, vertice_filter=vertice_filter, edge_filter=None
        )
    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
    with open(f"./filter_queries/{db_name}/graphs_vertices_all_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def graphs_edges_all_filtered(
    db_name: str, graph_filter: str, edge_filter: str, limit: str | None
) -> str:
    if db_name.startswith("mongo"):
        return all_mongodb_filter(
            graph_filter=graph_filter, vertice_filter=None, edge_filter=edge_filter
        )
    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_edges_all_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def graphs_all_filtered(
    db_name: str,
    graph_filter: str,
    vertice_filter: str,
    edge_filter: str,
    limit: str | None,
) -> str:
    if db_name.startswith("mongo"):
        return all_mongodb_filter(graph_filter, vertice_filter, edge_filter)

    suffix = make_suffix(db_name)
    if db_name == "graph_jsonb":
        vertice_filter = transform_query(vertice_filter, "v")
        edge_filter = transform_query(edge_filter, "e")
    with open(f"./filter_queries/{db_name}/graphs_all_filtered.{suffix}") as f:
        query = f.read()
        query = query.replace("{{graph_filter}}", graph_filter)
        query = query.replace("{{vertice_filter}}", vertice_filter)
        query = query.replace("{{edge_filter}}", edge_filter)
        if limit:
            query = query.replace("{{limit}}", limit)
        else:
            query = query.replace("{{limit}}", "")
            query = query.replace("LIMIT", "")
        return query


def make_suffix(db_name: str) -> str:
    if db_name.startswith("graph_"):
        return "sql"
    if db_name.startswith("neo4j"):
        return "cql"
    if db_name.startswith("mongo"):
        return "json"
    return "sql"
