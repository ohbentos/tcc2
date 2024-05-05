SELECT 
  graph_id
FROM 
  graphs g
WHERE 
  (
    SELECT bool_and(
      (
        SELECT bool_and(
        -- filter vertices here
          {{vertice_filter}}
        )
        FROM unnest(e.vertices) AS v(vertice)
      )
    )
    FROM unnest(edges) AS e(edge)
  ) 
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
