SELECT 
  graph_id
FROM 
  graphs g
WHERE 
  (
    SELECT bool_and(
      -- filter vertices here
      {{vertice_filter}}
    AND
      (
        SELECT bool_and(
          --  filter edges here
        {{edge_filter}}
        )
        FROM unnest(v.edges) AS e(edge)
      )
    )
    FROM unnest(vertices) AS v(vertice)
  ) 
AND (
  -- filter graphs here
  {{graph_filter}}
) LIMIT {{limit}};
