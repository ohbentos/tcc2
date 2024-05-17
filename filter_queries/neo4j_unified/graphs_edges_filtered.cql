MATCH (g:Props)-[:HAS_GRAPH_PROPS]-(:Vertice)-[e1:EDGE]-(:Vertice)
WHERE {{graph_filter}}
WITH g.graph_id as graph_id, COLLECT(e1) AS edges
WHERE
  ANY(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
