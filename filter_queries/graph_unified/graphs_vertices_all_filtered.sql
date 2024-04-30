SELECT 
  graph_id
FROM 
  graphs g
WHERE (
  SELECT bool_and(
    -- vertice filter
    {{vertice_filter}}
  )
  FROM unnest(vertices) AS v
)
AND (
    -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
