# MATCH (n) DETACH DELETE n

# MATCH (v:Vertice) RETURN valueType(v.p1)

# CREATE INDEX vertice_id_idx FOR (v:Vertice) ON (v.id);
# CREATE INDEX vertice_graph_id_idx FOR (v:Vertice) ON (v.graph_id);
# CREATE INDEX props_graph_id_idx FOR (p:Props) ON (p.graph_id);
# CREATE INDEX props_id_idx FOR (p:Props) ON (p.id);
# CREATE INDEX edge_graph_id_idx FOR ()-[r:EDGE]-() ON (r.graph_id);
# CREATE INDEX edge_id_idx FOR ()-[r:EDGE]-() ON (r.id);
# CREATE INDEX has_graph_props_graph_id_idx FOR ()-[r:HAS_GRAPH_PROPS]-() ON (r.graph_id);


BLA = ",".join([f"p{n}: prop.p{n}" for n in range(1, 318)])


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
        """
MATCH (:Vertice)-[e:EDGE]-(:Vertice)
RETURN e.graph_id, COLLECT(e)
"""
        + f"LIMIT {limit}": str(limit)
    }


def all_view_separated(limit: int) -> dict[str, str]:
    return {
        """
MATCH (p:Props)
MATCH (v:Vertice)-[e:EDGE]-(:Vertice)
WHERE p.graph_id = v.graph_id
RETURN p, COLLECT(e),COLLECT(v)
"""
        + f"LIMIT {limit}": str(limit)
    }


def all_view_unified(limit: int) -> dict[str, str]:
    return {
        """
MATCH (ve:Vertice)-[has_props:HAS_GRAPH_PROPS]->(p:Props)
MATCH (ve)-[ed:EDGE]-(:Vertice)
RETURN p, COLLECT(ed), COLLECT(ve)
"""
        + f"LIMIT {limit}": str(limit)
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


def create_bulk(tx, props, edges, vertices):
    query = (
        "UNWIND $props as prop "
        + "CREATE (v:Props:Graphs { "
        + f"graph_id: prop.graph_id,{BLA}"
        + " })"
    )
    tx.run(query, props=props)

    query = """
       UNWIND $vertices as vertice 
       CREATE (v:Vertice:Graphs { 
       id: vertice.id, 
       graph_id: vertice.graph_id, 
       p1: vertice.properties.p1, 
       p2: vertice.properties.p2, 
       p3: vertice.properties.p3, 
       p4: vertice.properties.p4, 
       p5: vertice.properties.p5, 
       p6: vertice.properties.p6, 
       p7: vertice.properties.p7, 
       p8: vertice.properties.p8, 
       p9: vertice.properties.p9, 
       p10: vertice.properties.p10
        })
    """
    tx.run(query, vertices=[item for sublist in vertices for item in sublist])

    tx.run(
        "UNWIND $edges as edge "
        "MATCH (v1:Vertice {id: edge.id1}), (v2:Vertice {id: edge.id2}) "
        "CREATE (v1)-[:EDGE { "
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
        edges=[item for sublist in edges for item in sublist],
    )


def create_vertice_separated(tx, vertex_id, graph_id, properties):
    tx.run(
        "CREATE (v:Vertice:Graphs {id: $id, graph_id: $graph_id, p1: $p1, p2: $p2, p3: $p3, p4: $p4, p5: $p5, "
        "p6: $p6, p7: $p7, p8: $p8, p9: $p9, p10: $p10})",
        id=vertex_id,
        graph_id=graph_id,
        **properties,
    )


def create_vertice_separated_bulk(tx, properties):
    tx.run(
        "UNWIND $vertices as vertice "
        "CREATE (v:Vertice:Graphs { "
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


def create_edge_separated_bulk(tx, properties):
    tx.run(
        "UNWIND $edges as edge "
        "MATCH (v1:Vertice {id: edge.id1}), (v2:Vertice {id: edge.id2}) "
        "CREATE (v1)-[:EDGE { "
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


def create_edge_separated(tx, id1, id2, graph_id, properties):
    tx.run(
        "MATCH (v1:Vertice {id: $id1}), (v2:Vertice {id: $id2}) "
        "CREATE (v1)-[r:EDGE {graph_id: $graph_id, p1: $p1, p2: $p2, p3: $p3, p4: $p4, p5: $p5, "
        "p6: $p6, p7: $p7, p8: $p8, p9: $p9, p10: $p10}]->(v2)",
        id1=id1,
        id2=id2,
        graph_id=graph_id,
        **properties,
    )


def create_props_link(tx, vertices_ids, graph_id):
    tx.run(
        "UNWIND $vertices_ids as vertice "
        "MATCH (v:Vertice {id: vertice}), (p:Props {graph_id: $graph_id}) "
        "CREATE (v)-[r:HAS_GRAPH_PROPS {graph_id: $graph_id"
        "}]->(p)",
        graph_id=graph_id,
        vertices_ids=vertices_ids,
    )


def create_props(tx, graph_id, properties):
    tx.run(
        "CREATE (v:Props:Graphs {"
        + "graph_id: $graph_id, "
        + ",".join([f"p{n}: $p{n}" for n in range(1, len(properties) + 1)])
        + "})",
        graph_id=graph_id,
        **properties,
    )
