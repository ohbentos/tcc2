SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
  SELECT 1
  FROM 
    unnest(edges) AS e(edge)
  WHERE 
  -- edges filter
  {{edge_filter}}
)
AND EXISTS (
  SELECT 1
  FROM 
    unnest(vertices) AS v(vertice)
  WHERE 
  -- vertices filter
  {{vertice_filter}}
)
AND (
  -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
