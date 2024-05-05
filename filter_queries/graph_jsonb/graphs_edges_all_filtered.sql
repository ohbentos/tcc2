SELECT 
  graph_id
FROM 
  graphs g
WHERE (
  SELECT bool_and(
    -- edges filter
    {{edge_filter}}
  )
  FROM jsonb_array_elements(edges) AS e
)
AND (
  --  graphs filter
  {{graph_filter}}
) LIMIT {{limit}};
