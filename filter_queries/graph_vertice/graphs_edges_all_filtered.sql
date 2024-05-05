SELECT 
  graph_id
FROM 
  graphs g
WHERE 
  (
    SELECT bool_and(
      (
        SELECT bool_and(
        -- filter edges here
          {{edge_filter}}
        )
        FROM unnest(v.edges) AS e(edge)
      )
    )
    FROM unnest(vertices) AS v(vertice)
  ) 
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
