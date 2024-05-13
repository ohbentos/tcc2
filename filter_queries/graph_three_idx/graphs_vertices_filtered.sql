SELECT DISTINCT
  v.graph_id
FROM
  vertices v
JOIN (
  SELECT
    graph_id
  FROM
    graphs g
  WHERE 
    -- graphs filters here
    {{graph_filter}}
) g ON g.graph_id = v.graph_id
WHERE
  -- vertice filters here
  {{vertice_filter}}
LIMIT {{limit}};
