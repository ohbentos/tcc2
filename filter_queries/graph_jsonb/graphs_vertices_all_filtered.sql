SELECT 
  graph_id
FROM 
  graphs g
WHERE (
  SELECT bool_and(
    -- vertices filter
    {{vertice_filter}}
  )
  FROM jsonb_array_elements(vertices) AS v
)
AND (
  --  graphs filter
  {{graph_filter}}
) LIMIT {{limit}};
