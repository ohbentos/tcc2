MATCH (g:Props) 
  WHERE {{graph_filter}}
WITH g
MATCH (ve:Vertice)-[ed:EDGE]-(:Vertice) 
  WHERE ve.graph_id = g.graph_id
WITH g.graph_id AS graph_id, COLLECT(ve) AS vertices, COLLECT(ed) AS edges
WHERE
  ALL(v IN vertices WHERE {{vertice_filter}} )
  AND
  ALL(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
