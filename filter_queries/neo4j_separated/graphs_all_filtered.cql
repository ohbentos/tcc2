MATCH (ve:Vertice)-[ed:EDGE]-(:Vertice)
WITH ve.graph_id AS graph_id, COLLECT(ve) AS vertices, COLLECT(ed) AS edges
MATCH (g:Props) WHERE g.graph_id = graph_id AND g.p1 > 4
WITH graph_id, vertices , edges, COLLECT(g) AS props
WHERE
  ALL(v IN vertices WHERE v.p1 > 2)
  AND
  ALL(e IN edges WHERE e.p1 > 2)
RETURN DISTINCT graph_id LIMIT {{limit}}
