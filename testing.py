query = """
MATCH (ve:Vertice)-[:HAS_GRAPH_PROPS]->(g:Props) 
WHERE g.p1 > 10
WITH ve
MATCH (ve)-[ed:EDGE]-(:Vertice)
WITH ed.graph_id AS graph_id, COLLECT(ed) AS edges
WHERE
  ANY(e IN edges WHERE e.p1 > 5 )
RETURN graph_id LIMIT 1
"""

# MATCH (p:Props)-[:HAS_GRAPH_PROPS]-(v:Vertices)
# WHERE p.p1 > 10
# WITH p, COLLECT(v) AS vertices
# WHERE ALL(v IN vertices WHERE v.p1 > 4)
# RETURN DISTINCT p.graph_id LIMIT 1

# MATCH (ve:Vertice)-[has_props:HAS_GRAPH_PROPS]->(g:Props) 
# WHERE g.p1 > 10
# WITH g.graph_id as graph_ids
# MATCH (:Vertice)-[ed:EDGE]-(:Vertice) WHERE ed.graph_id = graph_ids
# WITH ed.graph_id AS graph_id, COLLECT(ed) AS edges
# WHERE
#   ANY(e IN edges WHERE e.p1 > 5 )
# RETURN graph_id LIMIT 1

from neo4j import GraphDatabase

with GraphDatabase.driver(
    "bolt://127.0.0.1:3020",
    auth=("neo4j", "password"),
    # connection_timeout=5,
    # max_connection_lifetime=60,
    # max_connection_pool_size=100,
    # max_transaction_retry_time=1,
    # connection_acquisition_timeout=5,
) as driver:
    # with driver.session() as session:
    #     result = session.run("""
    #     MATCH (ve:Vertice)
    #     return ve LIMIT 100
    #     """)
    #     for record in result:
    #         print(record)
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            print(record)
