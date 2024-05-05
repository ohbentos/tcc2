SELECT 
  graph_id
FROM 
  graphs g
WHERE EXISTS (
    SELECT 1
    FROM 
      unnest(vertices) AS v
    WHERE
       -- vertices filter here
      {{vertice_filter}}
)
AND (
  -- graph filter here
  {{graph_filter}}
) LIMIT {{limit}};
