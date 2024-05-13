MATCH (g:Props) WHERE {{graph_filter}}
MATCH (ve:Vertice) WHERE ve.graph_id = g.graph_id
WITH ve.graph_id AS graph_id, COLLECT(ve) AS vertices
WHERE
  ANY(v IN vertices WHERE {{vertice_filter}} )
RETURN graph_id LIMIT {{limit}}
