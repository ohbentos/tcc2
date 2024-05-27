import json

import pymongo
from pymongo.collection import Collection

AUTH_MONGODB = ("mongodb", "password")


def graph_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {"vertices": 0, "edges": 0},
    }

    return {json.dumps(q): str(limit)}


def vertice_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {"vertices": 1},
    }

    return {json.dumps(q): str(limit)}


def edge_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {"edges": 1},
    }

    return {json.dumps(q): str(limit)}


def all_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {},
    }

    return {json.dumps(q): str(limit)}


def get_vertice_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {"vertices": 1},
    }

    return {json.dumps(q): str(limit)}


def get_edge_view(limit: int) -> dict[str, str]:
    q = {
        "query": {},
        "fields": {"edges": 1},
    }

    return {json.dumps(q): str(limit)}


def list_diameters() -> dict[str, str | None]:
    q = {
        "query": {"p5": {"$gt": 2}},
        "fields": {"p51": 1},
    }

    return {json.dumps(q): None}


def all_mongodb_filter(
    graph_filter=None,
    vertice_filter=None,
    edge_filter=None,
) -> str:
    query = create_query_all(
        graph_conditions=graph_filter,
        vertex_conditions=vertice_filter,
        edge_conditions=edge_filter,
    )

    out = {}
    out["query"] = query
    out["fields"] = {"_id": 0, "graph_id": 1}

    return json.dumps(out)


def mongodb_filter(
    graph_filter=None,
    vertice_filter=None,
    edge_filter=None,
) -> str:
    query = create_query(
        graph_conditions=graph_filter,
        vertex_conditions=vertice_filter,
        edge_conditions=edge_filter,
    )

    out = {}
    out["query"] = query
    out["fields"] = {"_id": 0, "graph_id": 1}

    return json.dumps(out)


class MongoDatabase:
    def __init__(self, port: int):
        self.port = port
        self.ref = "mongodb://127.0.0.1:" + str(self.port)

    def start(self) -> Collection:
        client = pymongo.MongoClient(
            self.ref,
            username=AUTH_MONGODB[0],
            password=AUTH_MONGODB[1],
        )
        self._client = client
        self.client = client["graphs"]["graphs"]
        return self.client

    def query(self, q: str, limit: str) -> int:
        print(q)
        query_json = json.loads(q)
        if "fields" in query_json:
            results = self.client.find(query_json["query"], query_json["fields"])
        else:
            results = self.client.find(query_json)

        if limit != "None":
            results = results.limit(int(limit))

        i = 0
        for _ in results:
            # print(r)
            i += 1

        self._client.close()
        return i


def create_query(
    vertex_conditions=None,
    edge_conditions=None,
    graph_conditions=None,
    vertex_prefix="v.",
    edge_prefix="e.",
    graph_prefix="g.",
) -> dict[str, list]:
    query_conditions = []

    # Parse vertex conditions if provided
    if vertex_conditions:
        vertex_condition_list = vertex_conditions.split("AND")
        parsed_vertex_conditions = []

        for condition in vertex_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the vertex prefix
            field = field.replace(vertex_prefix, "")
            # Map the operator to MongoDB operators
            mongo_operator = {
                ">": "$gt",
                "<": "$lt",
                ">=": "$gte",
                "<=": "$lte",
                "==": "$eq",
                "!=": "$ne",
            }.get(operator)
            # Append the parsed condition
            parsed_vertex_conditions.append({field: {mongo_operator: value}})

        # Create the $elemMatch part of the query for vertices
        vertex_query = {"vertices": {"$elemMatch": {"$and": parsed_vertex_conditions}}}
        query_conditions.append(vertex_query)

    # Parse edge conditions if provided
    if edge_conditions:
        edge_condition_list = edge_conditions.split("AND")
        parsed_edge_conditions = []

        for condition in edge_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the edge prefix
            field = field.replace(edge_prefix, "")
            # Map the operator to MongoDB operators
            mongo_operator = {
                ">": "$gt",
                "<": "$lt",
                ">=": "$gte",
                "<=": "$lte",
                "==": "$eq",
                "!=": "$ne",
            }.get(operator)
            # Append the parsed condition
            parsed_edge_conditions.append({field: {mongo_operator: value}})

        # Create the $elemMatch part of the query for edges
        edge_query = {"edges": {"$elemMatch": {"$and": parsed_edge_conditions}}}
        query_conditions.append(edge_query)

    # Parse graph conditions if provided
    if graph_conditions:
        graph_condition_list = graph_conditions.split("AND")
        parsed_graph_conditions = []

        for condition in graph_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the graph prefix
            field = field.replace(graph_prefix, "")
            # Map the operator to MongoDB operators
            mongo_operator = {
                ">": "$gt",
                "<": "$lt",
                ">=": "$gte",
                "<=": "$lte",
                "==": "$eq",
                "!=": "$ne",
            }.get(operator)
            # Append the parsed condition
            parsed_graph_conditions.append({field: {mongo_operator: value}})

        query_conditions.extend(parsed_graph_conditions)

    # Combine the conditions
    if query_conditions:
        query = {"$and": query_conditions}
    else:
        query = {}

    return query


def create_query_all(
    vertex_conditions=None,
    edge_conditions=None,
    graph_conditions=None,
    vertex_prefix="v.",
    edge_prefix="e.",
    graph_prefix="g.",
) -> dict[str, list]:
    query_conditions = []

    # Parse vertex conditions if provided
    if vertex_conditions:
        vertex_condition_list = vertex_conditions.split("AND")
        parsed_vertex_conditions = []

        for condition in vertex_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the vertex prefix
            field = field.replace(vertex_prefix, "")
            # Map the operator to the inverted MongoDB operators
            inverted_operator = {
                ">": "$lte",
                "<": "$gte",
                ">=": "$lt",
                "<=": "$gt",
                "==": "$ne",
                "!=": "$eq",
            }.get(operator)
            # Append the parsed condition
            parsed_vertex_conditions.append({field: {inverted_operator: value}})

        # Create the $not $elemMatch part of the query for vertices
        vertex_query = {
            "vertices": {"$not": {"$elemMatch": {"$or": parsed_vertex_conditions}}}
        }
        query_conditions.append(vertex_query)

    # Parse edge conditions if provided
    if edge_conditions:
        edge_condition_list = edge_conditions.split("AND")
        parsed_edge_conditions = []

        for condition in edge_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the edge prefix
            field = field.replace(edge_prefix, "")
            # Map the operator to the inverted MongoDB operators
            inverted_operator = {
                ">": "$lte",
                "<": "$gte",
                ">=": "$lt",
                "<=": "$gt",
                "==": "$ne",
                "!=": "$eq",
            }.get(operator)
            # Append the parsed condition
            parsed_edge_conditions.append({field: {inverted_operator: value}})

        # Create the $not $elemMatch part of the query for edges
        edge_query = {
            "edges": {"$not": {"$elemMatch": {"$or": parsed_edge_conditions}}}
        }
        query_conditions.append(edge_query)

    # Parse graph conditions if provided
    if graph_conditions:
        graph_condition_list = graph_conditions.split("AND")
        parsed_graph_conditions = []

        for condition in graph_condition_list:
            condition = condition.strip()
            field, operator, value = parse_condition(condition)
            # Remove the graph prefix
            field = field.replace(graph_prefix, "")
            # Map the operator to MongoDB operators
            mongo_operator = {
                ">": "$gt",
                "<": "$lt",
                ">=": "$gte",
                "<=": "$lte",
                "==": "$eq",
                "!=": "$ne",
            }.get(operator)
            # Append the parsed condition
            parsed_graph_conditions.append({field: {mongo_operator: value}})

        query_conditions.extend(parsed_graph_conditions)

    # Combine the conditions
    if query_conditions:
        query = {"$and": query_conditions}
    else:
        query = {}

    return query


def parse_condition(condition):
    # Split the condition by space to extract field, operator, and value
    parts = condition.split()
    field = parts[0]
    operator = parts[1]
    value = float(parts[2])  # Convert value to float
    return field, operator, value
