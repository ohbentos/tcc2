CREATE VIEW graph_view AS
SELECT
  p.graph_id,
  p.p1,
  p.p2, -- properties from the props table (need to fill)
  e.edges_info, -- all edges
  v.vertices_info -- all vertices
FROM
  props p
  CROSS JOIN LATERAL (
    SELECT
      json_agg (e) edges_info
    FROM
      edges e
    WHERE
      e.graph_id = p.graph_id
  ) e
  CROSS JOIN LATERAL (
    SELECT
      json_agg (v) vertices_info
    FROM
      vertices v
    WHERE
      v.graph_id = p.graph_id
  ) v;
