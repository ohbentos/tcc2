MATCH (g:Props)
  WHERE {{graph_filter}}
WITH g
MATCH (:Vertice)-[e:EDGE]-(:Vertice)
  WHERE g.graph_id = e.graph_id
WITH g.graph_id as graph_id,COLLECT(e) AS edges
WHERE
  ANY(e IN edges WHERE {{edge_filter}} )
RETURN graph_id LIMIT {{limit}}
