SELECT 
  graph_id
FROM 
  graphs g
WHERE (
  SELECT bool_and(
    -- edges filter
    {{edge_filter}}
  )
  FROM unnest(edges) AS e 
)
AND (
  SELECT bool_and(
    -- vertices filter
    {{vertice_filter}}
  )
  FROM unnest(vertices) AS v
)
AND (
  -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
