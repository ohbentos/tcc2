MATCH (g:Props)
  WHERE {{graph_filter}}
WITH g
MATCH (v:Vertice)-[:EDGE]-(:Vertice)
  WHERE g.graph_id = v.graph_id
WITH g.graph_id as graph_id,COLLECT(v) AS vertices
WHERE
  ALL(v IN vertices WHERE {{vertice_filter}} )
RETURN graph_id LIMIT {{limit}}
