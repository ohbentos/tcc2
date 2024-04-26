CREATE TABLE IF NOT EXISTS vertices (
  id uuid PRIMARY KEY,
  graph_id uuid NOT NULL,
  p1 real NOT NULL,
  p2 real NOT NULL,
  p3 real NOT NULL,
  p4 real NOT NULL,
  p5 real NOT NULL,
  p6 real NOT NULL,
  p7 real NOT NULL,
  p8 real NOT NULL,
  p9 real NOT NULL,
  p10 real NOT NULL
);

CREATE TABLE IF NOT EXISTS edges (
  id uuid PRIMARY KEY,
  graph_id uuid NOT NULL,
  vertice1 uuid NOT NULL,
  vertice2 uuid NOT NULL,
  p1 real NOT NULL,
  p2 real NOT NULL,
  p3 real NOT NULL,
  p4 real NOT NULL,
  p5 real NOT NULL,
  p6 real NOT NULL,
  p7 real NOT NULL,
  p8 real NOT NULL,
  p9 real NOT NULL,
  p10 real NOT NULL
);

CREATE TABLE IF NOT EXISTS props (
  graph_id uuid PRIMARY KEY,
  p1 real NOT NULL,
  p2 real NOT NULL,
  p3 real NOT NULL,
  p4 real NOT NULL,
  p5 real NOT NULL,
  p6 real NOT NULL,
  p7 real NOT NULL,
  p8 real NOT NULL,
  p9 real NOT NULL,
  p10 real NOT NULL,
  p11 real NOT NULL,
  p12 real NOT NULL,
  p13 real NOT NULL,
  p14 real NOT NULL,
  p15 real NOT NULL,
  p16 real NOT NULL,
  p17 real NOT NULL,
  p18 real NOT NULL,
  p19 real NOT NULL,
  p20 real NOT NULL,
  p21 real NOT NULL,
  p22 real NOT NULL,
  p23 real NOT NULL,
  p24 real NOT NULL,
  p25 real NOT NULL,
  p26 real NOT NULL,
  p27 real NOT NULL,
  p28 real NOT NULL,
  p29 real NOT NULL,
  p30 real NOT NULL,
  p31 real NOT NULL,
  p32 real NOT NULL,
  p33 real NOT NULL,
  p34 real NOT NULL,
  p35 real NOT NULL,
  p36 real NOT NULL,
  p37 real NOT NULL,
  p38 real NOT NULL,
  p39 real NOT NULL,
  p40 real NOT NULL,
  p41 real NOT NULL,
  p42 real NOT NULL,
  p43 real NOT NULL,
  p44 real NOT NULL,
  p45 real NOT NULL,
  p46 real NOT NULL,
  p47 real NOT NULL,
  p48 real NOT NULL,
  p49 real NOT NULL,
  p50 real NOT NULL,
  p51 real NOT NULL,
  p52 real NOT NULL,
  p53 real NOT NULL,
  p54 real NOT NULL,
  p55 real NOT NULL,
  p56 real NOT NULL,
  p57 real NOT NULL,
  p58 real NOT NULL,
  p59 real NOT NULL,
  p60 real NOT NULL,
  p61 real NOT NULL,
  p62 real NOT NULL,
  p63 real NOT NULL,
  p64 real NOT NULL,
  p65 real NOT NULL,
  p66 real NOT NULL,
  p67 real NOT NULL,
  p68 real NOT NULL,
  p69 real NOT NULL,
  p70 real NOT NULL,
  p71 real NOT NULL,
  p72 real NOT NULL,
  p73 real NOT NULL,
  p74 real NOT NULL,
  p75 real NOT NULL,
  p76 real NOT NULL,
  p77 real NOT NULL,
  p78 real NOT NULL,
  p79 real NOT NULL,
  p80 real NOT NULL,
  p81 real NOT NULL,
  p82 real NOT NULL,
  p83 real NOT NULL,
  p84 real NOT NULL,
  p85 real NOT NULL,
  p86 real NOT NULL,
  p87 real NOT NULL,
  p88 real NOT NULL,
  p89 real NOT NULL,
  p90 real NOT NULL,
  p91 real NOT NULL,
  p92 real NOT NULL,
  p93 real NOT NULL,
  p94 real NOT NULL,
  p95 real NOT NULL,
  p96 real NOT NULL,
  p97 real NOT NULL,
  p98 real NOT NULL,
  p99 real NOT NULL,
  p100 real NOT NULL,
  p101 real NOT NULL,
  p102 real NOT NULL,
  p103 real NOT NULL,
  p104 real NOT NULL,
  p105 real NOT NULL,
  p106 real NOT NULL,
  p107 real NOT NULL,
  p108 real NOT NULL,
  p109 real NOT NULL,
  p110 real NOT NULL,
  p111 real NOT NULL,
  p112 real NOT NULL,
  p113 real NOT NULL,
  p114 real NOT NULL,
  p115 real NOT NULL,
  p116 real NOT NULL,
  p117 real NOT NULL,
  p118 real NOT NULL,
  p119 real NOT NULL,
  p120 real NOT NULL,
  p121 real NOT NULL,
  p122 real NOT NULL,
  p123 real NOT NULL,
  p124 real NOT NULL,
  p125 real NOT NULL,
  p126 real NOT NULL,
  p127 real NOT NULL,
  p128 real NOT NULL,
  p129 real NOT NULL,
  p130 real NOT NULL,
  p131 real NOT NULL,
  p132 real NOT NULL,
  p133 real NOT NULL,
  p134 real NOT NULL,
  p135 real NOT NULL,
  p136 real NOT NULL,
  p137 real NOT NULL,
  p138 real NOT NULL,
  p139 real NOT NULL,
  p140 real NOT NULL,
  p141 real NOT NULL,
  p142 real NOT NULL,
  p143 real NOT NULL,
  p144 real NOT NULL,
  p145 real NOT NULL,
  p146 real NOT NULL,
  p147 real NOT NULL,
  p148 real NOT NULL,
  p149 real NOT NULL,
  p150 real NOT NULL,
  p151 real NOT NULL,
  p152 real NOT NULL,
  p153 real NOT NULL,
  p154 real NOT NULL,
  p155 real NOT NULL,
  p156 real NOT NULL,
  p157 real NOT NULL,
  p158 real NOT NULL,
  p159 real NOT NULL,
  p160 real NOT NULL,
  p161 real NOT NULL,
  p162 real NOT NULL,
  p163 real NOT NULL,
  p164 real NOT NULL,
  p165 real NOT NULL,
  p166 real NOT NULL,
  p167 real NOT NULL,
  p168 real NOT NULL,
  p169 real NOT NULL,
  p170 real NOT NULL,
  p171 real NOT NULL,
  p172 real NOT NULL,
  p173 real NOT NULL,
  p174 real NOT NULL,
  p175 real NOT NULL,
  p176 real NOT NULL,
  p177 real NOT NULL,
  p178 real NOT NULL,
  p179 real NOT NULL,
  p180 real NOT NULL,
  p181 real NOT NULL,
  p182 real NOT NULL,
  p183 real NOT NULL,
  p184 real NOT NULL,
  p185 real NOT NULL,
  p186 real NOT NULL,
  p187 real NOT NULL,
  p188 real NOT NULL,
  p189 real NOT NULL,
  p190 real NOT NULL,
  p191 real NOT NULL,
  p192 real NOT NULL,
  p193 real NOT NULL,
  p194 real NOT NULL,
  p195 real NOT NULL,
  p196 real NOT NULL,
  p197 real NOT NULL,
  p198 real NOT NULL,
  p199 real NOT NULL,
  p200 real NOT NULL,
  p201 real NOT NULL,
  p202 real NOT NULL,
  p203 real NOT NULL,
  p204 real NOT NULL,
  p205 real NOT NULL,
  p206 real NOT NULL,
  p207 real NOT NULL,
  p208 real NOT NULL,
  p209 real NOT NULL,
  p210 real NOT NULL,
  p211 real NOT NULL,
  p212 real NOT NULL,
  p213 real NOT NULL,
  p214 real NOT NULL,
  p215 real NOT NULL,
  p216 real NOT NULL,
  p217 real NOT NULL,
  p218 real NOT NULL,
  p219 real NOT NULL,
  p220 real NOT NULL,
  p221 real NOT NULL,
  p222 real NOT NULL,
  p223 real NOT NULL,
  p224 real NOT NULL,
  p225 real NOT NULL,
  p226 real NOT NULL,
  p227 real NOT NULL,
  p228 real NOT NULL,
  p229 real NOT NULL,
  p230 real NOT NULL,
  p231 real NOT NULL,
  p232 real NOT NULL,
  p233 real NOT NULL,
  p234 real NOT NULL,
  p235 real NOT NULL,
  p236 real NOT NULL,
  p237 real NOT NULL,
  p238 real NOT NULL,
  p239 real NOT NULL,
  p240 real NOT NULL,
  p241 real NOT NULL,
  p242 real NOT NULL,
  p243 real NOT NULL,
  p244 real NOT NULL,
  p245 real NOT NULL,
  p246 real NOT NULL,
  p247 real NOT NULL,
  p248 real NOT NULL,
  p249 real NOT NULL,
  p250 real NOT NULL,
  p251 real NOT NULL,
  p252 real NOT NULL,
  p253 real NOT NULL,
  p254 real NOT NULL,
  p255 real NOT NULL,
  p256 real NOT NULL,
  p257 real NOT NULL,
  p258 real NOT NULL,
  p259 real NOT NULL,
  p260 real NOT NULL,
  p261 real NOT NULL,
  p262 real NOT NULL,
  p263 real NOT NULL,
  p264 real NOT NULL,
  p265 real NOT NULL,
  p266 real NOT NULL,
  p267 real NOT NULL,
  p268 real NOT NULL,
  p269 real NOT NULL,
  p270 real NOT NULL,
  p271 real NOT NULL,
  p272 real NOT NULL,
  p273 real NOT NULL,
  p274 real NOT NULL,
  p275 real NOT NULL,
  p276 real NOT NULL,
  p277 real NOT NULL,
  p278 real NOT NULL,
  p279 real NOT NULL,
  p280 real NOT NULL,
  p281 real NOT NULL,
  p282 real NOT NULL,
  p283 real NOT NULL,
  p284 real NOT NULL,
  p285 real NOT NULL,
  p286 real NOT NULL,
  p287 real NOT NULL,
  p288 real NOT NULL,
  p289 real NOT NULL,
  p290 real NOT NULL,
  p291 real NOT NULL,
  p292 real NOT NULL,
  p293 real NOT NULL,
  p294 real NOT NULL,
  p295 real NOT NULL,
  p296 real NOT NULL,
  p297 real NOT NULL,
  p298 real NOT NULL,
  p299 real NOT NULL,
  p300 real NOT NULL,
  p301 real NOT NULL,
  p302 real NOT NULL,
  p303 real NOT NULL,
  p304 real NOT NULL,
  p305 real NOT NULL,
  p306 real NOT NULL,
  p307 real NOT NULL,
  p308 real NOT NULL,
  p309 real NOT NULL,
  p310 real NOT NULL,
  p311 real NOT NULL,
  p312 real NOT NULL,
  p313 real NOT NULL,
  p314 real NOT NULL,
  p315 real NOT NULL,
  p316 real NOT NULL,
  p317 real NOT NULL
);

CREATE VIEW graph_view_arr AS
SELECT
  p.*,
  e.edges_info, -- all edges
  v.vertices_info -- all vertices
FROM
  props p
  CROSS JOIN LATERAL (
    SELECT
      array_agg (e) edges_info
    FROM
      edges e
    WHERE
      e.graph_id = p.graph_id
  ) e
  CROSS JOIN LATERAL (
    SELECT
      array_agg (v) vertices_info
    FROM
      vertices v
    WHERE
      v.graph_id = p.graph_id
  ) v;

CREATE VIEW graph_view_json AS
SELECT
  p.*,
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

CREATE VIEW all_view_arr AS
SELECT
  g.*
FROM
  graph_view_arr g;

CREATE VIEW all_view_arr_json AS
SELECT
  g.*
FROM
  graph_view_json g;

CREATE VIEW graph_view AS
SELECT
  g.*
FROM
  props g;

CREATE VIEW edge_view AS
SELECT
  graph_id,
  jsonb_agg (
    json_build_object (
      'id',
      id,
      'vertice1',
      vertice1,
      'vertice2',
      vertice2,
      'p1',
      p1,
      'p2',
      p2,
      'p3',
      p3,
      'p4',
      p4,
      'p5',
      p5,
      'p6',
      p6,
      'p7',
      p7,
      'p8',
      p8,
      'p9',
      p9,
      'p10',
      p10
    )
  ) as edges
FROM
  edges
GROUP BY
  graph_id;

CREATE VIEW vertice_view AS
SELECT
  graph_id,
  jsonb_agg (
    json_build_object (
      'id',
      id,
      'p1',
      p1,
      'p2',
      p2,
      'p3',
      p3,
      'p4',
      p4,
      'p5',
      p5,
      'p6',
      p6,
      'p7',
      p7,
      'p8',
      p8,
      'p9',
      p9,
      'p10',
      p10
    )
  ) as vertices
FROM
  vertices
GROUP BY
  graph_id;

CREATE VIEW get_vertice_view AS
SELECT
  vertices.*
FROM
  vertices;

CREATE VIEW get_edge_view AS
SELECT
  edges.*
FROM
  edges;
