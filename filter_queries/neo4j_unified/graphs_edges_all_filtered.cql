MATCH (ve:Vertice)-[has_props:HAS_GRAPH_PROPS]->(g:Props) WHERE {{graph_filter}}
MATCH (ve)-[ed:EDGE]-(:Vertice)
WITH ed.graph_id AS graph_id, COLLECT(ed) AS edges
WHERE
  ALL(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
