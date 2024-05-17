MATCH (g:Props)-[:HAS_GRAPH_PROPS]-(v1:Vertice)-[e1:EDGE]-(:Vertice)
WHERE {{graph_filter}}
WITH g.graph_id as graph_id, COLLECT(v1) AS vertices, COLLECT(e1) AS edges
WHERE
  ALL(v IN vertices WHERE {{vertice_filter}} )
  AND
  ALL(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
