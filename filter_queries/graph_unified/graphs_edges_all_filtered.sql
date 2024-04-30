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
    -- graph filter
  {{graph_filter}}
) LIMIT {{limit}};
