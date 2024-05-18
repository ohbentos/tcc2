MATCH (g:Props)-[:HAS_GRAPH_PROPS]-(v1:Vertice)
WHERE {{graph_filter}}
WITH g.graph_id as graph_id, COLLECT(v1) AS vertices
WHERE
  ALL(v IN vertices WHERE {{vertice_filter}} )
RETURN graph_id LIMIT {{limit}}
