# MATCH (n) DETACH DELETE n
from neo4j import GraphDatabase, ManagedTransaction, Result

from db import neo4j

# MATCH (v:Vertice) RETURN valueType(v.p1)

# CREATE INDEX vertice_id_idx FOR (v:Vertice) ON (v.id);
# CREATE INDEX vertice_graph_id_idx FOR (v:Vertice) ON (v.graph_id);
# CREATE INDEX props_graph_id_idx FOR (p:Props) ON (p.graph_id);
# CREATE INDEX props_id_idx FOR (p:Props) ON (p.id);
# CREATE INDEX edge_graph_id_idx FOR ()-[r:EDGE]-() ON (r.graph_id);
# CREATE INDEX edge_id_idx FOR ()-[r:EDGE]-() ON (r.id);
# CREATE INDEX has_graph_props_graph_id_idx FOR ()-[r:HAS_GRAPH_PROPS]-() ON (r.graph_id);


def do_query(tx: ManagedTransaction, query: str) -> Result:
    return tx.run(query)  # type: ignore


class Neo4jDatabase:
    def __init__(self, port: int):
        self.port = port
        self.ref = "bolt://127.0.0.1:" + str(self.port)
        # print(self.ref)

    def start(self):
        self.driver = GraphDatabase.driver(
            self.ref,
            auth=neo4j.AUTH_NEO4J,
            max_connection_lifetime=3600,
            connection_timeout=3600,
            max_transaction_retry_time=300,
        )
        self.session = self.driver.session()

    def query(self, q: str, limit: str | None) -> int:
        results = self.session.run(q)  # type: ignore
        i = 0
        for _ in results:
            i += 1
        self.session.close()
        self.driver.close()
        return i


AUTH_NEO4J = ("neo4j", "password")


def graph_view(limit: int) -> dict[str, str]:
    return {
        """
MATCH (p:Props) RETURN p
"""
        + f"LIMIT {limit}": str(limit)
    }


def vertice_view(limit: int) -> dict[str, str]:
    return {
        """
MATCH (v:Vertice)
RETURN v.graph_id,COLLECT(v)
"""
        + f"LIMIT {limit}": str(limit)
    }


def edge_view(limit: int) -> dict[str, str]:
    return {
        "MATCH (:Vertice)-[e:EDGE]->(:Vertice) "
        "WITH DISTINCT e.graph_id AS graph_id "
        f"LIMIT {limit} "
        "MATCH ()-[edge:EDGE]->() "
        "WHERE edge.graph_id = graph_id "
        "RETURN graph_id, COLLECT(edge.graph_id) AS edges ": str(limit)
    }


def all_view_separated(limit: int) -> dict[str, str]:
    return {
        "MATCH (p:Props) "
        "WITH DISTINCT p.graph_id AS graph_id,p"
        f"LIMIT {limit} "
        "MATCH (ve:Vertice)-[ed:EDGE]-(:Vertice) "
        "WHERE ve.graph_id = graph_id AND ed.graph_id = graph_id "
        "RETURN p, COLLECT(ed), COLLECT(ve) ": str(limit)
    }


def all_view_unified(limit: int) -> dict[str, str]:
    return {
        "MATCH (ve:Vertice)-[has_props:HAS_GRAPH_PROPS]->(p:Props) "
        "WITH DISTINCT p.graph_id AS graph_id,p "
        f"LIMIT {limit} "
        "MATCH (ve:Vertice)-[ed:EDGE]-(:Vertice) "
        "WHERE ve.graph_id = graph_id AND ed.graph_id = graph_id "
        "RETURN p, COLLECT(ed), COLLECT(ve) ": str(limit)
    }


def get_vertice_view(limit: int) -> dict[str, str]:
    return {
        """
MATCH (v:Vertice)
RETURN v
"""
        + f"LIMIT {limit}": str(limit)
    }


def get_edge_view(limit: int) -> dict[str, str]:
    return {
        """
MATCH (:Vertice)-[e:EDGE]-(:Vertice)
RETURN e
"""
        + f"LIMIT {limit}": str(limit)
    }


def create_vertices(tx, properties):
    tx.run(
        "UNWIND $vertices as vertice "
        "CREATE (v:Vertice { "
        "id: vertice.id, "
        "graph_id: vertice.graph_id, "
        "p1: vertice.properties.p1, "
        "p2: vertice.properties.p2, "
        "p3: vertice.properties.p3, "
        "p4: vertice.properties.p4, "
        "p5: vertice.properties.p5, "
        "p6: vertice.properties.p6, "
        "p7: vertice.properties.p7, "
        "p8: vertice.properties.p8, "
        "p9: vertice.properties.p9, "
        "p10: vertice.properties.p10 "
        "})",
        **properties,
    )


def create_edges(tx, properties):
    tx.run(
        "UNWIND $edges as edge "
        "MATCH (v1:Vertice {id: edge.id1}), (v2:Vertice {id: edge.id2}) "
        "CREATE (v1)-[:EDGE { "
        "id: edge.id, "
        "graph_id: edge.graph_id, "
        "p1: edge.properties.p1, "
        "p2: edge.properties.p2, "
        "p3: edge.properties.p3, "
        "p4: edge.properties.p4, "
        "p5: edge.properties.p5, "
        "p6: edge.properties.p6, "
        "p7: edge.properties.p7, "
        "p8: edge.properties.p8, "
        "p9: edge.properties.p9, "
        "p10: edge.properties.p10 "
        "}]->(v2)",
        **properties,
    )


def create_props_link(tx, vertices_ids, graph_id):
    tx.run(
        "UNWIND $vertices_ids as vertice "
        "MATCH (v:Vertice {id: vertice}), (p:Props {graph_id: $graph_id}) "
        "CREATE (v)-[r:HAS_GRAPH_PROPS {"
        "graph_id: $graph_id,"
        "id: apoc.create.uuid()"
        "}]->(p)",
        graph_id=graph_id,
        vertices_ids=vertices_ids,
    )


def create_props(tx, graph_id, id, properties):
    tx.run(
        "CREATE (v:Props {"
        + " id: $id, "
        + "graph_id: $graph_id, "
        + ",".join([f"p{n}: $p{n}" for n in range(1, len(properties) + 1)])
        + "})",
        id=id,
        graph_id=graph_id,
        **properties,
    )


def run_neo4j_indexes(session):
    session.run(
        "CREATE CONSTRAINT unique_props_graph_id IF NOT EXISTS FOR (u:Props) REQUIRE u.graph_id IS UNIQUE"
    )
    session.run(
        "CREATE CONSTRAINT unique_props_id IF NOT EXISTS FOR (p:Props) REQUIRE p.id IS UNIQUE"
    )

    session.run(
        "CREATE CONSTRAINT unique_vertice_id IF NOT EXISTS FOR (v:Vertice) REQUIRE v.id IS UNIQUE"
    )
    session.run(
        "CREATE INDEX vertice_graph_id_idx IF NOT EXISTS FOR (v:Vertice) ON v.graph_id"
    )

    session.run(
        "CREATE CONSTRAINT unique_edge_id IF NOT EXISTS FOR ()-[e:EDGE]-() REQUIRE e.id IS UNIQUE"
    )
    session.run(
        "CREATE INDEX edge_graph_id_idx IF NOT EXISTS FOR ()-[e:EDGE]-() ON e.graph_id"
    )

    session.run(
        "CREATE CONSTRAINT unique_has_graph_props IF NOT EXISTS FOR ()-[r:HAS_GRAPH_PROPS]-() REQUIRE r.id IS UNIQUE"
    )
    session.run(
        "CREATE INDEX has_graph_props_idx IF NOT EXISTS FOR ()-[r:HAS_GRAPH_PROPS]-() ON r.graph_id"
    )
