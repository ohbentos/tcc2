SELECT DISTINCT
  e.graph_id
FROM
  edges e
JOIN (
  SELECT
    graph_id
  FROM
    graphs g
  WHERE 
    -- graphs filters here
    {{graph_filter}}
) g ON g.graph_id = e.graph_id
WHERE
  -- edges filters here
  {{edge_filter}}
LIMIT {{limit}};
