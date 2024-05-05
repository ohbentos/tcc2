SELECT 
  graph_id
FROM 
  graphs g
WHERE 
  (
    SELECT bool_and(
        -- filter vertices here
      {{vertice_filter}}
    )
    FROM unnest(vertices) AS v(vertice)
  ) 
AND (
  -- filter graphs here
  {{graph_filter}}
) LIMIT {{limit}};

