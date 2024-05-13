SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
    -- edges filter
    {{edge_filter}}
    ) AS edge_filter
  FROM
    edges e
  GROUP BY
    graph_id
) ef ON g.graph_id = ef.graph_id
WHERE
  ef.edge_filter
AND
  --  graphs filter
  {{graph_filter}}
LIMIT {{limit}};
