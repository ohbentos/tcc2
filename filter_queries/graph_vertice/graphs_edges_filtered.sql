SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
  SELECT 1
  FROM unnest(vertices) AS v(vertice)
    WHERE EXISTS (
      SELECT 1
      FROM 
        unnest(v.edges) AS e(edge)
      WHERE 
        (
         -- edges filter here
          {{edge_filter}}
        )
    )
)
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
