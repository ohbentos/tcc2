SELECT 
  graph_id
FROM 
  graphs g
WHERE 
  (
    SELECT bool_and(
        -- filter edges here
    {{edge_filter}}
    )
    FROM unnest(edges) AS e(edge)
  ) 
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
