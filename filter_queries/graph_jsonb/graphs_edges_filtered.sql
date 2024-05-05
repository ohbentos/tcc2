SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
  SELECT 1
  FROM 
    jsonb_array_elements(edges) AS e(edge)
  WHERE 
  -- edge filter
  {{edge_filter}}
)
AND (
  -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
