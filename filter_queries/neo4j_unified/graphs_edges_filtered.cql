MATCH (g:Props) WHERE {{graph_filter}}
MATCH (:Vertice)-[ed:EDGE]-(:Vertice) WHERE ed.graph_id = g.graph_id
WITH ed.graph_id AS graph_id,COLLECT(ed) AS edges
WHERE
  ANY(e IN edges WHERE {{edge_filter}} )
RETURN DISTINCT graph_id LIMIT {{limit}}
