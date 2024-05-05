SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
  SELECT 1
  FROM 
    jsonb_array_elements(vertices) AS v(vertice)
  WHERE 
  -- vertice filter
  {{vertice_filter}}
)
AND (
  -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
