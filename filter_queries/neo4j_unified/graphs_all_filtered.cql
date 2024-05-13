MATCH (ve:Vertice)-[has_props:HAS_GRAPH_PROPS]->(g:Props) WHERE {{graph_filter}}
MATCH (ve)-[ed:EDGE]-(:Vertice)
WITH ve.graph_id AS graph_id, COLLECT(ve) AS vertices, COLLECT(ed) AS edges
WHERE
  ALL(v IN vertices WHERE {{vertice_filter}} )
  AND
  ALL(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
