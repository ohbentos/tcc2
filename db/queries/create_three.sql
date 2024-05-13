CREATE TABLE IF NOT EXISTS vertices (
  id uuid PRIMARY KEY,
  graph_id uuid NOT NULL,
  p1 real NOT NULL, p2 real NOT NULL, p3 real NOT NULL, p4 real NOT NULL, p5 real NOT NULL, p6 real NOT NULL, p7 real NOT NULL, p8 real NOT NULL, p9 real NOT NULL, p10 real NOT NULL
);

CREATE TABLE IF NOT EXISTS edges (
  id uuid PRIMARY KEY,
  graph_id uuid NOT NULL,
  vertice1 uuid NOT NULL,
  vertice2 uuid NOT NULL,
  p1 real NOT NULL, p2 real NOT NULL, p3 real NOT NULL, p4 real NOT NULL, p5 real NOT NULL, p6 real NOT NULL, p7 real NOT NULL, p8 real NOT NULL, p9 real NOT NULL, p10 real NOT NULL
);

CREATE TABLE IF NOT EXISTS graphs (
  graph_id uuid PRIMARY KEY,
  p1 real NOT NULL, p2 real NOT NULL, p3 real NOT NULL, p4 real NOT NULL, p5 real NOT NULL, p6 real NOT NULL, p7 real NOT NULL, p8 real NOT NULL, p9 real NOT NULL, p10 real NOT NULL, p11 real NOT NULL, p12 real NOT NULL, p13 real NOT NULL, p14 real NOT NULL, p15 real NOT NULL, p16 real NOT NULL, p17 real NOT NULL, p18 real NOT NULL, p19 real NOT NULL, p20 real NOT NULL, p21 real NOT NULL, p22 real NOT NULL, p23 real NOT NULL, p24 real NOT NULL, p25 real NOT NULL, p26 real NOT NULL, p27 real NOT NULL, p28 real NOT NULL, p29 real NOT NULL, p30 real NOT NULL, p31 real NOT NULL, p32 real NOT NULL, p33 real NOT NULL, p34 real NOT NULL, p35 real NOT NULL, p36 real NOT NULL, p37 real NOT NULL, p38 real NOT NULL, p39 real NOT NULL, p40 real NOT NULL, p41 real NOT NULL, p42 real NOT NULL, p43 real NOT NULL, p44 real NOT NULL, p45 real NOT NULL, p46 real NOT NULL, p47 real NOT NULL, p48 real NOT NULL, p49 real NOT NULL, p50 real NOT NULL, p51 real NOT NULL, p52 real NOT NULL, p53 real NOT NULL, p54 real NOT NULL, p55 real NOT NULL, p56 real NOT NULL, p57 real NOT NULL, p58 real NOT NULL, p59 real NOT NULL, p60 real NOT NULL, p61 real NOT NULL, p62 real NOT NULL, p63 real NOT NULL, p64 real NOT NULL, p65 real NOT NULL, p66 real NOT NULL, p67 real NOT NULL, p68 real NOT NULL, p69 real NOT NULL, p70 real NOT NULL, p71 real NOT NULL, p72 real NOT NULL, p73 real NOT NULL, p74 real NOT NULL, p75 real NOT NULL, p76 real NOT NULL, p77 real NOT NULL, p78 real NOT NULL, p79 real NOT NULL, p80 real NOT NULL, p81 real NOT NULL, p82 real NOT NULL, p83 real NOT NULL, p84 real NOT NULL, p85 real NOT NULL, p86 real NOT NULL, p87 real NOT NULL, p88 real NOT NULL, p89 real NOT NULL, p90 real NOT NULL, p91 real NOT NULL, p92 real NOT NULL, p93 real NOT NULL, p94 real NOT NULL, p95 real NOT NULL, p96 real NOT NULL, p97 real NOT NULL, p98 real NOT NULL, p99 real NOT NULL, p100 real NOT NULL, p101 real NOT NULL, p102 real NOT NULL, p103 real NOT NULL, p104 real NOT NULL, p105 real NOT NULL, p106 real NOT NULL, p107 real NOT NULL, p108 real NOT NULL, p109 real NOT NULL, p110 real NOT NULL, p111 real NOT NULL, p112 real NOT NULL, p113 real NOT NULL, p114 real NOT NULL, p115 real NOT NULL, p116 real NOT NULL, p117 real NOT NULL, p118 real NOT NULL, p119 real NOT NULL, p120 real NOT NULL, p121 real NOT NULL, p122 real NOT NULL, p123 real NOT NULL, p124 real NOT NULL, p125 real NOT NULL, p126 real NOT NULL, p127 real NOT NULL, p128 real NOT NULL, p129 real NOT NULL, p130 real NOT NULL, p131 real NOT NULL, p132 real NOT NULL, p133 real NOT NULL, p134 real NOT NULL, p135 real NOT NULL, p136 real NOT NULL, p137 real NOT NULL, p138 real NOT NULL, p139 real NOT NULL, p140 real NOT NULL, p141 real NOT NULL, p142 real NOT NULL, p143 real NOT NULL, p144 real NOT NULL, p145 real NOT NULL, p146 real NOT NULL, p147 real NOT NULL, p148 real NOT NULL, p149 real NOT NULL, p150 real NOT NULL, p151 real NOT NULL, p152 real NOT NULL, p153 real NOT NULL, p154 real NOT NULL, p155 real NOT NULL, p156 real NOT NULL, p157 real NOT NULL, p158 real NOT NULL, p159 real NOT NULL, p160 real NOT NULL, p161 real NOT NULL, p162 real NOT NULL, p163 real NOT NULL, p164 real NOT NULL, p165 real NOT NULL, p166 real NOT NULL, p167 real NOT NULL, p168 real NOT NULL, p169 real NOT NULL, p170 real NOT NULL, p171 real NOT NULL, p172 real NOT NULL, p173 real NOT NULL, p174 real NOT NULL, p175 real NOT NULL, p176 real NOT NULL, p177 real NOT NULL, p178 real NOT NULL, p179 real NOT NULL, p180 real NOT NULL, p181 real NOT NULL, p182 real NOT NULL, p183 real NOT NULL, p184 real NOT NULL, p185 real NOT NULL, p186 real NOT NULL, p187 real NOT NULL, p188 real NOT NULL, p189 real NOT NULL, p190 real NOT NULL, p191 real NOT NULL, p192 real NOT NULL, p193 real NOT NULL, p194 real NOT NULL, p195 real NOT NULL, p196 real NOT NULL, p197 real NOT NULL, p198 real NOT NULL, p199 real NOT NULL, p200 real NOT NULL, p201 real NOT NULL, p202 real NOT NULL, p203 real NOT NULL, p204 real NOT NULL, p205 real NOT NULL, p206 real NOT NULL, p207 real NOT NULL, p208 real NOT NULL, p209 real NOT NULL, p210 real NOT NULL, p211 real NOT NULL, p212 real NOT NULL, p213 real NOT NULL, p214 real NOT NULL, p215 real NOT NULL, p216 real NOT NULL, p217 real NOT NULL, p218 real NOT NULL, p219 real NOT NULL, p220 real NOT NULL, p221 real NOT NULL, p222 real NOT NULL, p223 real NOT NULL, p224 real NOT NULL, p225 real NOT NULL, p226 real NOT NULL, p227 real NOT NULL, p228 real NOT NULL, p229 real NOT NULL, p230 real NOT NULL, p231 real NOT NULL, p232 real NOT NULL, p233 real NOT NULL, p234 real NOT NULL, p235 real NOT NULL, p236 real NOT NULL, p237 real NOT NULL, p238 real NOT NULL, p239 real NOT NULL, p240 real NOT NULL, p241 real NOT NULL, p242 real NOT NULL, p243 real NOT NULL, p244 real NOT NULL, p245 real NOT NULL, p246 real NOT NULL, p247 real NOT NULL, p248 real NOT NULL, p249 real NOT NULL, p250 real NOT NULL, p251 real NOT NULL, p252 real NOT NULL, p253 real NOT NULL, p254 real NOT NULL, p255 real NOT NULL, p256 real NOT NULL, p257 real NOT NULL, p258 real NOT NULL, p259 real NOT NULL, p260 real NOT NULL, p261 real NOT NULL, p262 real NOT NULL, p263 real NOT NULL, p264 real NOT NULL, p265 real NOT NULL, p266 real NOT NULL, p267 real NOT NULL, p268 real NOT NULL, p269 real NOT NULL, p270 real NOT NULL, p271 real NOT NULL, p272 real NOT NULL, p273 real NOT NULL, p274 real NOT NULL, p275 real NOT NULL, p276 real NOT NULL, p277 real NOT NULL, p278 real NOT NULL, p279 real NOT NULL, p280 real NOT NULL, p281 real NOT NULL, p282 real NOT NULL, p283 real NOT NULL, p284 real NOT NULL, p285 real NOT NULL, p286 real NOT NULL, p287 real NOT NULL, p288 real NOT NULL, p289 real NOT NULL, p290 real NOT NULL, p291 real NOT NULL, p292 real NOT NULL, p293 real NOT NULL, p294 real NOT NULL, p295 real NOT NULL, p296 real NOT NULL, p297 real NOT NULL, p298 real NOT NULL, p299 real NOT NULL, p300 real NOT NULL, p301 real NOT NULL, p302 real NOT NULL, p303 real NOT NULL, p304 real NOT NULL, p305 real NOT NULL, p306 real NOT NULL, p307 real NOT NULL, p308 real NOT NULL, p309 real NOT NULL, p310 real NOT NULL, p311 real NOT NULL, p312 real NOT NULL, p313 real NOT NULL, p314 real NOT NULL, p315 real NOT NULL, p316 real NOT NULL, p317 real NOT NULL
);

-- CREATE INDEX IF NOT EXISTS vertices_graph_id_idx ON vertices (graph_id);
-- CREATE INDEX IF NOT EXISTS edges_graph_id_idx ON edges (graph_id);

DROP VIEW IF EXISTS graph_view;
CREATE OR REPLACE VIEW graph_view AS
SELECT
  g.*
FROM
  graphs g;

DROP VIEW IF EXISTS vertice_view;
CREATE OR REPLACE VIEW vertice_view AS
SELECT 
  graph_id,
  array_agg(vertices) AS vertices
FROM 
  vertices
GROUP BY 
  graph_id;

DROP VIEW IF EXISTS edge_view;
CREATE OR REPLACE VIEW edge_view AS
SELECT 
  graph_id,
  array_agg(edges) as edges
FROM 
  edges
GROUP BY 
  graph_id;

DROP VIEW IF EXISTS all_view;
CREATE OR REPLACE VIEW all_view AS
SELECT 
    g.graph_id, g.p1, g.p2,g.p3,g.p4,g.p5,g.p6,g.p7,g.p8,g.p9,g.p10,g.p11,g.p12,g.p13,g.p14,g.p15,g.p16,g.p17,g.p18,g.p19,g.p20,g.p21,g.p22,g.p23,g.p24,g.p25,g.p26,g.p27,g.p28,g.p29,g.p30,g.p31,g.p32,g.p33,g.p34,g.p35,g.p36,g.p37,g.p38,g.p39,g.p40,g.p41,g.p42,g.p43,g.p44,g.p45,g.p46,g.p47,g.p48,g.p49,g.p50,g.p51,g.p52,g.p53,g.p54,g.p55,g.p56,g.p57,g.p58,g.p59,g.p60,g.p61,g.p62,g.p63,g.p64,g.p65,g.p66,g.p67,g.p68,g.p69,g.p70,g.p71,g.p72,g.p73,g.p74,g.p75,g.p76,g.p77,g.p78,g.p79,g.p80,g.p81,g.p82,g.p83,g.p84,g.p85,g.p86,g.p87,g.p88,g.p89,g.p90,g.p91,g.p92,g.p93,g.p94,g.p95,g.p96,g.p97,g.p98,g.p99,g.p100,g.p101,g.p102,g.p103,g.p104,g.p105,g.p106,g.p107,g.p108,g.p109,g.p110,g.p111,g.p112,g.p113,g.p114,g.p115,g.p116,g.p117,g.p118,g.p119,g.p120,g.p121,g.p122,g.p123,g.p124,g.p125,g.p126,g.p127,g.p128,g.p129,g.p130,g.p131,g.p132,g.p133,g.p134,g.p135,g.p136,g.p137,g.p138,g.p139,g.p140,g.p141,g.p142,g.p143,g.p144,g.p145,g.p146,g.p147,g.p148,g.p149,g.p150,g.p151,g.p152,g.p153,g.p154,g.p155,g.p156,g.p157,g.p158,g.p159,g.p160,g.p161,g.p162,g.p163,g.p164,g.p165,g.p166,g.p167,g.p168,g.p169,g.p170,g.p171,g.p172,g.p173,g.p174,g.p175,g.p176,g.p177,g.p178,g.p179,g.p180,g.p181,g.p182,g.p183,g.p184,g.p185,g.p186,g.p187,g.p188,g.p189,g.p190,g.p191,g.p192,g.p193,g.p194,g.p195,g.p196,g.p197,g.p198,g.p199,g.p200,g.p201,g.p202,g.p203,g.p204,g.p205,g.p206,g.p207,g.p208,g.p209,g.p210,g.p211,g.p212,g.p213,g.p214,g.p215,g.p216,g.p217,g.p218,g.p219,g.p220,g.p221,g.p222,g.p223,g.p224,g.p225,g.p226,g.p227,g.p228,g.p229,g.p230,g.p231,g.p232,g.p233,g.p234,g.p235,g.p236,g.p237,g.p238,g.p239,g.p240,g.p241,g.p242,g.p243,g.p244,g.p245,g.p246,g.p247,g.p248,g.p249,g.p250,g.p251,g.p252,g.p253,g.p254,g.p255,g.p256,g.p257,g.p258,g.p259,g.p260,g.p261,g.p262,g.p263,g.p264,g.p265,g.p266,g.p267,g.p268,g.p269,g.p270,g.p271,g.p272,g.p273,g.p274,g.p275,g.p276,g.p277,g.p278,g.p279,g.p280,g.p281,g.p282,g.p283,g.p284,g.p285,g.p286,g.p287,g.p288,g.p289,g.p290,g.p291,g.p292,g.p293,g.p294,g.p295,g.p296,g.p297,g.p298,g.p299,g.p300,g.p301,g.p302,g.p303,g.p304,g.p305,g.p306,g.p307,g.p308,g.p309,g.p310,g.p311,g.p312,g.p313,g.p314,g.p315,g.p316,g.p317,
    edges.edges,
    vertices.vertices
FROM 
    graphs g,
    vertice_view vertices,
    edge_view edges;

DROP VIEW IF EXISTS get_vertice_view;
CREATE OR REPLACE VIEW get_vertice_view AS
SELECT
  vertices.*
FROM
  vertices;

DROP VIEW IF EXISTS get_edge_view;
CREATE OR REPLACE VIEW get_edge_view AS
SELECT
  edges.*
FROM
  edges;

-- selects graph_id from vertices with ONE or more vertices with filter cond
DROP VIEW IF EXISTS graphs_vertices_filtered_view;
CREATE OR REPLACE VIEW graphs_vertices_filtered_view AS
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
    g.p1 > 15
) g ON g.graph_id = v.graph_id
WHERE
  -- vertice filters here
  v.p1 > 5;

-- selects graph_id from graphs with ONE or more vertices with filter cond
DROP VIEW IF EXISTS graphs_edges_filtered_view;
CREATE OR REPLACE VIEW graphs_edges_filtered_view AS
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
    g.p1 > 15
) g ON g.graph_id = e.graph_id
WHERE
  -- edges filters here
  e.p1 > 5;

-- select graph_ids from graphs with ONE or more vertices and edges with filter cond
-- SELECT DISTINCT graph_id FROM ( SELECT * FROM graphs_edges_filtered_view WHERE g_p1 > 15 AND e_p1 < 10 AND v_p1 < 10) AS graph_ids LIMIT 1;
  -- g.p1 AS g_p1,g.p2 AS g_p2,g.p3 AS g_p3,g.p4 AS g_p4,g.p5 AS g_p5,g.p6 AS g_p6,g.p7 AS g_p7,g.p8 AS g_p8,g.p9 AS g_p9,g.p10 AS g_p10,g.p11 AS g_p11,g.p12 AS g_p12,g.p13 AS g_p13,g.p14 AS g_p14,g.p15 AS g_p15,g.p16 AS g_p16,g.p17 AS g_p17,g.p18 AS g_p18,g.p19 AS g_p19,g.p20 AS g_p20,g.p21 AS g_p21,g.p22 AS g_p22,g.p23 AS g_p23,g.p24 AS g_p24,g.p25 AS g_p25,g.p26 AS g_p26,g.p27 AS g_p27,g.p28 AS g_p28,g.p29 AS g_p29,g.p30 AS g_p30,g.p31 AS g_p31,g.p32 AS g_p32,g.p33 AS g_p33,g.p34 AS g_p34,g.p35 AS g_p35,g.p36 AS g_p36,g.p37 AS g_p37,g.p38 AS g_p38,g.p39 AS g_p39,g.p40 AS g_p40,g.p41 AS g_p41,g.p42 AS g_p42,g.p43 AS g_p43,g.p44 AS g_p44,g.p45 AS g_p45,g.p46 AS g_p46,g.p47 AS g_p47,g.p48 AS g_p48,g.p49 AS g_p49,g.p50 AS g_p50,g.p51 AS g_p51,g.p52 AS g_p52,g.p53 AS g_p53,g.p54 AS g_p54,g.p55 AS g_p55,g.p56 AS g_p56,g.p57 AS g_p57,g.p58 AS g_p58,g.p59 AS g_p59,g.p60 AS g_p60,g.p61 AS g_p61,g.p62 AS g_p62,g.p63 AS g_p63,g.p64 AS g_p64,g.p65 AS g_p65,g.p66 AS g_p66,g.p67 AS g_p67,g.p68 AS g_p68,g.p69 AS g_p69,g.p70 AS g_p70,g.p71 AS g_p71,g.p72 AS g_p72,g.p73 AS g_p73,g.p74 AS g_p74,g.p75 AS g_p75,g.p76 AS g_p76,g.p77 AS g_p77,g.p78 AS g_p78,g.p79 AS g_p79,g.p80 AS g_p80,g.p81 AS g_p81,g.p82 AS g_p82,g.p83 AS g_p83,g.p84 AS g_p84,g.p85 AS g_p85,g.p86 AS g_p86,g.p87 AS g_p87,g.p88 AS g_p88,g.p89 AS g_p89,g.p90 AS g_p90,g.p91 AS g_p91,g.p92 AS g_p92,g.p93 AS g_p93,g.p94 AS g_p94,g.p95 AS g_p95,g.p96 AS g_p96,g.p97 AS g_p97,g.p98 AS g_p98,g.p99 AS g_p99,g.p100 AS g_p100,g.p101 AS g_p101,g.p102 AS g_p102,g.p103 AS g_p103,g.p104 AS g_p104,g.p105 AS g_p105,g.p106 AS g_p106,g.p107 AS g_p107,g.p108 AS g_p108,g.p109 AS g_p109,g.p110 AS g_p110,g.p111 AS g_p111,g.p112 AS g_p112,g.p113 AS g_p113,g.p114 AS g_p114,g.p115 AS g_p115,g.p116 AS g_p116,g.p117 AS g_p117,g.p118 AS g_p118,g.p119 AS g_p119,g.p120 AS g_p120,g.p121 AS g_p121,g.p122 AS g_p122,g.p123 AS g_p123,g.p124 AS g_p124,g.p125 AS g_p125,g.p126 AS g_p126,g.p127 AS g_p127,g.p128 AS g_p128,g.p129 AS g_p129,g.p130 AS g_p130,g.p131 AS g_p131,g.p132 AS g_p132,g.p133 AS g_p133,g.p134 AS g_p134,g.p135 AS g_p135,g.p136 AS g_p136,g.p137 AS g_p137,g.p138 AS g_p138,g.p139 AS g_p139,g.p140 AS g_p140,g.p141 AS g_p141,g.p142 AS g_p142,g.p143 AS g_p143,g.p144 AS g_p144,g.p145 AS g_p145,g.p146 AS g_p146,g.p147 AS g_p147,g.p148 AS g_p148,g.p149 AS g_p149,g.p150 AS g_p150,g.p151 AS g_p151,g.p152 AS g_p152,g.p153 AS g_p153,g.p154 AS g_p154,g.p155 AS g_p155,g.p156 AS g_p156,g.p157 AS g_p157,g.p158 AS g_p158,g.p159 AS g_p159,g.p160 AS g_p160,g.p161 AS g_p161,g.p162 AS g_p162,g.p163 AS g_p163,g.p164 AS g_p164,g.p165 AS g_p165,g.p166 AS g_p166,g.p167 AS g_p167,g.p168 AS g_p168,g.p169 AS g_p169,g.p170 AS g_p170,g.p171 AS g_p171,g.p172 AS g_p172,g.p173 AS g_p173,g.p174 AS g_p174,g.p175 AS g_p175,g.p176 AS g_p176,g.p177 AS g_p177,g.p178 AS g_p178,g.p179 AS g_p179,g.p180 AS g_p180,g.p181 AS g_p181,g.p182 AS g_p182,g.p183 AS g_p183,g.p184 AS g_p184,g.p185 AS g_p185,g.p186 AS g_p186,g.p187 AS g_p187,g.p188 AS g_p188,g.p189 AS g_p189,g.p190 AS g_p190,g.p191 AS g_p191,g.p192 AS g_p192,g.p193 AS g_p193,g.p194 AS g_p194,g.p195 AS g_p195,g.p196 AS g_p196,g.p197 AS g_p197,g.p198 AS g_p198,g.p199 AS g_p199,g.p200 AS g_p200,g.p201 AS g_p201,g.p202 AS g_p202,g.p203 AS g_p203,g.p204 AS g_p204,g.p205 AS g_p205,g.p206 AS g_p206,g.p207 AS g_p207,g.p208 AS g_p208,g.p209 AS g_p209,g.p210 AS g_p210,g.p211 AS g_p211,g.p212 AS g_p212,g.p213 AS g_p213,g.p214 AS g_p214,g.p215 AS g_p215,g.p216 AS g_p216,g.p217 AS g_p217,g.p218 AS g_p218,g.p219 AS g_p219,g.p220 AS g_p220,g.p221 AS g_p221,g.p222 AS g_p222,g.p223 AS g_p223,g.p224 AS g_p224,g.p225 AS g_p225,g.p226 AS g_p226,g.p227 AS g_p227,g.p228 AS g_p228,g.p229 AS g_p229,g.p230 AS g_p230,g.p231 AS g_p231,g.p232 AS g_p232,g.p233 AS g_p233,g.p234 AS g_p234,g.p235 AS g_p235,g.p236 AS g_p236,g.p237 AS g_p237,g.p238 AS g_p238,g.p239 AS g_p239,g.p240 AS g_p240,g.p241 AS g_p241,g.p242 AS g_p242,g.p243 AS g_p243,g.p244 AS g_p244,g.p245 AS g_p245,g.p246 AS g_p246,g.p247 AS g_p247,g.p248 AS g_p248,g.p249 AS g_p249,g.p250 AS g_p250,g.p251 AS g_p251,g.p252 AS g_p252,g.p253 AS g_p253,g.p254 AS g_p254,g.p255 AS g_p255,g.p256 AS g_p256,g.p257 AS g_p257,g.p258 AS g_p258,g.p259 AS g_p259,g.p260 AS g_p260,g.p261 AS g_p261,g.p262 AS g_p262,g.p263 AS g_p263,g.p264 AS g_p264,g.p265 AS g_p265,g.p266 AS g_p266,g.p267 AS g_p267,g.p268 AS g_p268,g.p269 AS g_p269,g.p270 AS g_p270,g.p271 AS g_p271,g.p272 AS g_p272,g.p273 AS g_p273,g.p274 AS g_p274,g.p275 AS g_p275,g.p276 AS g_p276,g.p277 AS g_p277,g.p278 AS g_p278,g.p279 AS g_p279,g.p280 AS g_p280,g.p281 AS g_p281,g.p282 AS g_p282,g.p283 AS g_p283,g.p284 AS g_p284,g.p285 AS g_p285,g.p286 AS g_p286,g.p287 AS g_p287,g.p288 AS g_p288,g.p289 AS g_p289,g.p290 AS g_p290,g.p291 AS g_p291,g.p292 AS g_p292,g.p293 AS g_p293,g.p294 AS g_p294,g.p295 AS g_p295,g.p296 AS g_p296,g.p297 AS g_p297,g.p298 AS g_p298,g.p299 AS g_p299,g.p300 AS g_p300,g.p301 AS g_p301,g.p302 AS g_p302,g.p303 AS g_p303,g.p304 AS g_p304,g.p305 AS g_p305,g.p306 AS g_p306,g.p307 AS g_p307,g.p308 AS g_p308,g.p309 AS g_p309,g.p310 AS g_p310,g.p311 AS g_p311,g.p312 AS g_p312,g.p313 AS g_p313,g.p314 AS g_p314,g.p315 AS g_p315,g.p316 AS g_p316,g.p317 AS g_p317,
  -- e.id AS e_id, e.p1 AS e_p1, e.p2 AS e_p2, e.p3 AS e_p3, e.p4 AS e_p4, e.p5 AS e_p5, e.p6 AS e_p6, e.p7 AS e_p7, e.p8 AS e_p8, e.p9 AS e_p9, e.p10 AS e_p10,
  -- v.id AS v_id, v.p1 AS v_p1, v.p2 AS v_p2, v.p3 AS v_p3, v.p4 AS v_p4, v.p5 AS v_p5, v.p6 AS v_p6, v.p7 AS v_p7, v.p8 AS v_p8, v.p9 AS v_p9, v.p10 AS v_p10
DROP VIEW IF EXISTS graphs_filtered_view;
CREATE OR REPLACE VIEW graphs_filtered_view AS
SELECT DISTINCT
  g.graph_id
FROM
  graphs g
JOIN
  vertices v ON g.graph_id = v.graph_id
JOIN
  edges e ON g.graph_id = e.graph_id
WHERE
  --  vertice filter
  v.p1 > 9
  --  graphs filter
  AND g.p1 > 9;

 -- example filter all vertices
DROP VIEW IF EXISTS graphs_vertices_all_filtered_view;
CREATE OR REPLACE VIEW graphs_vertices_all_filtered_view AS
SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
      --  vertice filter
      p1 > 5
    ) AS vertice_filter
  FROM
    edges
  GROUP BY
    graph_id
) v ON g.graph_id = v.graph_id
WHERE
  v.vertice_filter 
AND 
  --  graphs filter
  g.p1> 15;

 -- example filter all edges
DROP VIEW IF EXISTS graphs_edges_all_filtered_view;
CREATE OR REPLACE VIEW graphs_edges_all_filtered_view AS
SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
    -- edges filter
      p1 > 5
    ) AS edge_filter
  FROM
    edges
  GROUP BY
    graph_id
) e ON g.graph_id = e.graph_id
WHERE
  e.edge_filter
AND
  --  graphs filter
  g.p1 > 0;

-- filters all edges and vertices
DROP VIEW IF EXISTS graphs_all_filtered_view;
CREATE OR REPLACE VIEW graphs_all_filtered_view AS
SELECT
  g.graph_id
FROM
  graphs g
JOIN (
  SELECT
    graph_id,
    bool_and(
      -- edge filters here
      p1 > 10
    ) AS edge_filter
  FROM
    edges
  GROUP BY
    graph_id
) e ON g.graph_id = e.graph_id AND e.edge_filter
JOIN (
  SELECT
    graph_id,
    bool_and(
      -- vertice filters here
      p1 > 10
    ) AS vertice_filter
  FROM
    vertices
  GROUP BY
    graph_id
) v ON g.graph_id = v.graph_id AND v.vertice_filter
WHERE
  --  graphs filter
  g.p1 > 10;
