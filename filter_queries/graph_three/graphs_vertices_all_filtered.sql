SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
      --  vertice filter
      {{vertice_filter}}
    ) AS vertice_filter
  FROM
    vertices v
  GROUP BY
    graph_id
) vf ON g.graph_id = vf.graph_id
WHERE
  vf.vertice_filter 
AND 
  --  graphs filter
  {{graph_filter}}
LIMIT {{limit}};
