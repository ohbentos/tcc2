SELECT
  jsonb_agg (p1_p2_object) AS result
FROM
  (
    SELECT
      jsonb_build_object (
        'number_of_vertices',
        p1,
        'number_of_edges',
        p2,
        'diameter_distribution',
        jsonb_agg (
          jsonb_build_object ('diameter', p51, 'count', count)
        )
      ) AS p1_p2_object
    FROM
      (
        SELECT
          p1,
          p2,
          p51,
          COUNT(*) AS count
        FROM
          graphs
        GROUP BY
          p1,
          p2,
          p51
        ORDER BY
          p1,
          p2,
          p51
      ) AS subquery
    GROUP BY
      p1,
      p2
    ORDER BY
      p1,
      p2
  ) AS final_query;

-- SELECT
--   jsonb_agg (p1_object) AS result
-- FROM
--   (
--     SELECT
--       jsonb_build_object (
--         'number_of_vertices',
--         p1,
--         'diameter_distribution',
--         jsonb_agg (
--           jsonb_build_object ('diameter', p51, 'count', count)
--         )
--       ) AS p1_object
--     FROM
--       (
--         SELECT
--           p1,
--           p51,
--           COUNT(*) AS count
--         FROM
--           graphs
--         GROUP BY
--           p1,
--           p51
--         ORDER BY
--           p1,
--           p51
--       ) AS subquery
--     GROUP BY
--       p1
--     ORDER BY
--       p1
--   ) AS final_query;
-- SELECT
--   jsonb_agg (p2_object) AS result
-- FROM
--   (
--     SELECT
--       jsonb_build_object (
--         'number_of_edges',
--         p2,
--         'diameter_distribution',
--         jsonb_agg (
--           jsonb_build_object ('diameter', p51, 'count', count)
--         )
--       ) AS p2_object
--     FROM
--       (
--         SELECT
--           p2,
--           p51,
--           COUNT(*) AS count
--         FROM
--           graphs
--         GROUP BY
--           p2,
--           p51
--         ORDER BY
--           p2,
--           p51
--       ) AS subquery
--     GROUP BY
--       p2
--     ORDER BY
--       p2
--   ) AS final_query;
