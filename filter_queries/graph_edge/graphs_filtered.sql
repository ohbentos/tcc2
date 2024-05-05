SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
  SELECT 1
  FROM unnest(edges) AS e(edge)
    WHERE (
      -- edges filter here
      {{edge_filter}}
    )
    AND EXISTS (
      SELECT 1
      FROM 
        unnest(e.vertices) AS v(vertice)
      WHERE 
        (
         -- vertices filter here
          {{vertice_filter}}
        )
    )
)
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
