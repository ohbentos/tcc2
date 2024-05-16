import tqdm
from neo4j import GraphDatabase


def batch_process_relationships(uri, user, password, batch_size):
    driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_distinct_graph_ids(session):
        query = "MATCH (p:Props) RETURN p.graph_id as graph_id"
        result = session.run(query)
        return [record["graph_id"] for record in result]

    def link_vertices_to_props(session, graph_id):
        query = (
            "MATCH (v:Vertice), (p:Props) "
            "WHERE v.graph_id = $graph_id AND p.graph_id = $graph_id "
            "MERGE (v)-[:HAS_GRAPH_PROPS]->(p)"
        )
        session.run(query, graph_id=graph_id)

    with driver.session() as session:
        graph_ids = get_distinct_graph_ids(session)
        print("got_all_graph_ids")
        for graph_id in tqdm.tqdm(graph_ids):
            link_vertices_to_props(session, graph_id)

    driver.close()

def batch_process_insert_id_edge(uri, user, password, batch_size):
    driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_distinct_graph_ids(session):
        query = "MATCH (p:Props) RETURN p.graph_id as graph_id"
        result = session.run(query)
        return [record["graph_id"] for record in result]

    def link_vertices_to_props(session, graph_id):
        query = (
            "MATCH ()-[e:EDGE]-() WHERE e.graph_id = $graph_id "
            "SET e.id = apoc.create.uuid()"
        )
        session.run(query, graph_id=graph_id)

    with driver.session() as session:
        graph_ids = get_distinct_graph_ids(session)
        print("got all graph ids")
        for graph_id in tqdm.tqdm(graph_ids):
            link_vertices_to_props(session, graph_id)

    driver.close()


# Example usage
uri = "bolt://localhost:3020"
user = "neo4j"
password = "password"

# batch_process_relationships(uri, user, password, None)
# batch_process_insert_id_edge(uri, user, password, None)
