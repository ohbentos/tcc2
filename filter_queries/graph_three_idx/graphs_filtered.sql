SELECT DISTINCT
  g.graph_id
FROM
  graphs g
JOIN
  vertices v ON g.graph_id = v.graph_id
JOIN
  edges e ON g.graph_id = e.graph_id
WHERE
  --  vertice filter
  {{vertice_filter}}
  AND 
  --  edge filter
  {{edge_filter}}
  AND 
  --  graphs filter
  {{graph_filter}}
LIMIT {{limit}};
