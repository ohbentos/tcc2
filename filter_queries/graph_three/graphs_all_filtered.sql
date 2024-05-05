SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
      -- edge filters here
    {{edge_filter}}
    ) AS edge_filter
  FROM
    edges e
  GROUP BY
    graph_id
) ef ON g.graph_id = ef.graph_id AND ef.edge_filter
JOIN (
  SELECT
    graph_id,
    bool_and(
      -- vertice filters here
    {{vertice_filter}}
    ) AS vertice_filter
  FROM
    vertices v
  GROUP BY
    graph_id
) vf ON g.graph_id = vf.graph_id AND vf.vertice_filter
WHERE
  --  graphs filter
  {{graph_filter}}
LIMIT {{limit}};
