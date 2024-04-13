import time

import psycopg2
import psycopg2.extras


class PGDatabase:
    def __init__(self, port: int):
        self.port = port
        self.ref = "postgres://127.0.0.1:" + str(self.port)
        # self.start()

    def start(self):
        self.conn = psycopg2.connect(
            database="postgres",
            host="127.0.0.1",
            user="postgres",
            password="postgres",
            port=self.port,
        )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def print(self, s):
        time.sleep(3)
        print(s)

    def start_and_execute(self, s: str) -> float:
        start = time.monotonic()
        self.start()
        self.cur.execute(s)
        end = time.monotonic()
        return end - start

    def execute(self, s: str):
        self.cur.execute(s)

    def executemany(self, q, s):
        self.cur.executemany(q, s)

    def finish(self):
        self.cur.close()

    def __str__(self):
        return self.ref

    def execute_parallel_query(self, query):
        self.start()
        self.cur.execute(query)
        records = self.cur.fetchall()
        self.conn.close()

        return list(records)

    def create_db(self, restart):
        if restart == True:
            self.cur.execute("DROP TABLE IF EXISTS props")
            self.cur.execute("DROP TABLE IF EXISTS vertices")
            self.cur.execute("DROP TABLE IF EXISTS edges")
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS vertices (
                id uuid PRIMARY KEY,
                graph_id uuid NOT NULL,
                p1 real NULL,
                p2 real NULL,
                p3 real NULL,
                p4 real NULL,
                p5 real NULL,
                p6 real NULL,
                p7 real NULL,
                p8 real NULL,
                p9 real NULL,
                p10 real NULL
            )
        """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS edges (
                id uuid PRIMARY KEY,
                graph_id uuid NOT NULL,
                vertice1 uuid NOT NULL,
                vertice2 uuid NOT NULL,
                p1 real NULL,
                p2 real NULL,
                p3 real NULL,
                p4 real NULL,
                p5 real NULL,
                p6 real NULL,
                p7 real NULL,
                p8 real NULL,
                p9 real NULL,
                p10 real NULL
            )
        """
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS props (
            graph_id uuid PRIMARY KEY,
            p1 real NULL,
            p2 real NULL,
            p3 real NULL,
            p4 real NULL,
            p5 real NULL,
            p6 real NULL,
            p7 real NULL,
            p8 real NULL,
            p9 real NULL,
            p10 real NULL,
            p11 real NULL,
            p12 real NULL,
            p13 real NULL,
            p14 real NULL,
            p15 real NULL,
            p16 real NULL,
            p17 real NULL,
            p18 real NULL,
            p19 real NULL,
            p20 real NULL,
            p21 real NULL,
            p22 real NULL,
            p23 real NULL,
            p24 real NULL,
            p25 real NULL,
            p26 real NULL,
            p27 real NULL,
            p28 real NULL,
            p29 real NULL,
            p30 real NULL,
            p31 real NULL,
            p32 real NULL,
            p33 real NULL,
            p34 real NULL,
            p35 real NULL,
            p36 real NULL,
            p37 real NULL,
            p38 real NULL,
            p39 real NULL,
            p40 real NULL,
            p41 real NULL,
            p42 real NULL,
            p43 real NULL,
            p44 real NULL,
            p45 real NULL,
            p46 real NULL,
            p47 real NULL,
            p48 real NULL,
            p49 real NULL,
            p50 real NULL,
            p51 real NULL,
            p52 real NULL,
            p53 real NULL,
            p54 real NULL,
            p55 real NULL,
            p56 real NULL,
            p57 real NULL,
            p58 real NULL,
            p59 real NULL,
            p60 real NULL,
            p61 real NULL,
            p62 real NULL,
            p63 real NULL,
            p64 real NULL,
            p65 real NULL,
            p66 real NULL,
            p67 real NULL,
            p68 real NULL,
            p69 real NULL,
            p70 real NULL,
            p71 real NULL,
            p72 real NULL,
            p73 real NULL,
            p74 real NULL,
            p75 real NULL,
            p76 real NULL,
            p77 real NULL,
            p78 real NULL,
            p79 real NULL,
            p80 real NULL,
            p81 real NULL,
            p82 real NULL,
            p83 real NULL,
            p84 real NULL,
            p85 real NULL,
            p86 real NULL,
            p87 real NULL,
            p88 real NULL,
            p89 real NULL,
            p90 real NULL,
            p91 real NULL,
            p92 real NULL,
            p93 real NULL,
            p94 real NULL,
            p95 real NULL,
            p96 real NULL,
            p97 real NULL,
            p98 real NULL,
            p99 real NULL,
            p100 real NULL,
            p101 real NULL,
            p102 real NULL,
            p103 real NULL,
            p104 real NULL,
            p105 real NULL,
            p106 real NULL,
            p107 real NULL,
            p108 real NULL,
            p109 real NULL,
            p110 real NULL,
            p111 real NULL,
            p112 real NULL,
            p113 real NULL,
            p114 real NULL,
            p115 real NULL,
            p116 real NULL,
            p117 real NULL,
            p118 real NULL,
            p119 real NULL,
            p120 real NULL,
            p121 real NULL,
            p122 real NULL,
            p123 real NULL,
            p124 real NULL,
            p125 real NULL,
            p126 real NULL,
            p127 real NULL,
            p128 real NULL,
            p129 real NULL,
            p130 real NULL,
            p131 real NULL,
            p132 real NULL,
            p133 real NULL,
            p134 real NULL,
            p135 real NULL,
            p136 real NULL,
            p137 real NULL,
            p138 real NULL,
            p139 real NULL,
            p140 real NULL,
            p141 real NULL,
            p142 real NULL,
            p143 real NULL,
            p144 real NULL,
            p145 real NULL,
            p146 real NULL,
            p147 real NULL,
            p148 real NULL,
            p149 real NULL,
            p150 real NULL,
            p151 real NULL,
            p152 real NULL,
            p153 real NULL,
            p154 real NULL,
            p155 real NULL,
            p156 real NULL,
            p157 real NULL,
            p158 real NULL,
            p159 real NULL,
            p160 real NULL,
            p161 real NULL,
            p162 real NULL,
            p163 real NULL,
            p164 real NULL,
            p165 real NULL,
            p166 real NULL,
            p167 real NULL,
            p168 real NULL,
            p169 real NULL,
            p170 real NULL,
            p171 real NULL,
            p172 real NULL,
            p173 real NULL,
            p174 real NULL,
            p175 real NULL,
            p176 real NULL,
            p177 real NULL,
            p178 real NULL,
            p179 real NULL,
            p180 real NULL,
            p181 real NULL,
            p182 real NULL,
            p183 real NULL,
            p184 real NULL,
            p185 real NULL,
            p186 real NULL,
            p187 real NULL,
            p188 real NULL,
            p189 real NULL,
            p190 real NULL,
            p191 real NULL,
            p192 real NULL,
            p193 real NULL,
            p194 real NULL,
            p195 real NULL,
            p196 real NULL,
            p197 real NULL,
            p198 real NULL,
            p199 real NULL,
            p200 real NULL,
            p201 real NULL,
            p202 real NULL,
            p203 real NULL,
            p204 real NULL,
            p205 real NULL,
            p206 real NULL,
            p207 real NULL,
            p208 real NULL,
            p209 real NULL,
            p210 real NULL,
            p211 real NULL,
            p212 real NULL,
            p213 real NULL,
            p214 real NULL,
            p215 real NULL,
            p216 real NULL,
            p217 real NULL,
            p218 real NULL,
            p219 real NULL,
            p220 real NULL,
            p221 real NULL,
            p222 real NULL,
            p223 real NULL,
            p224 real NULL,
            p225 real NULL,
            p226 real NULL,
            p227 real NULL,
            p228 real NULL,
            p229 real NULL,
            p230 real NULL,
            p231 real NULL,
            p232 real NULL,
            p233 real NULL,
            p234 real NULL,
            p235 real NULL,
            p236 real NULL,
            p237 real NULL,
            p238 real NULL,
            p239 real NULL,
            p240 real NULL,
            p241 real NULL,
            p242 real NULL,
            p243 real NULL,
            p244 real NULL,
            p245 real NULL,
            p246 real NULL,
            p247 real NULL,
            p248 real NULL,
            p249 real NULL,
            p250 real NULL,
            p251 real NULL,
            p252 real NULL,
            p253 real NULL,
            p254 real NULL,
            p255 real NULL,
            p256 real NULL,
            p257 real NULL,
            p258 real NULL,
            p259 real NULL,
            p260 real NULL,
            p261 real NULL,
            p262 real NULL,
            p263 real NULL,
            p264 real NULL,
            p265 real NULL,
            p266 real NULL,
            p267 real NULL,
            p268 real NULL,
            p269 real NULL,
            p270 real NULL,
            p271 real NULL,
            p272 real NULL,
            p273 real NULL,
            p274 real NULL,
            p275 real NULL,
            p276 real NULL,
            p277 real NULL,
            p278 real NULL,
            p279 real NULL,
            p280 real NULL,
            p281 real NULL,
            p282 real NULL,
            p283 real NULL,
            p284 real NULL,
            p285 real NULL,
            p286 real NULL,
            p287 real NULL,
            p288 real NULL,
            p289 real NULL,
            p290 real NULL,
            p291 real NULL,
            p292 real NULL,
            p293 real NULL,
            p294 real NULL,
            p295 real NULL,
            p296 real NULL,
            p297 real NULL,
            p298 real NULL,
            p299 real NULL,
            p300 real NULL,
            p301 real NULL,
            p302 real NULL,
            p303 real NULL,
            p304 real NULL,
            p305 real NULL,
            p306 real NULL,
            p307 real NULL,
            p308 real NULL,
            p309 real NULL,
            p310 real NULL,
            p311 real NULL,
            p312 real NULL,
            p313 real NULL,
            p314 real NULL,
            p315 real NULL,
            p316 real NULL,
            p317 real NULL,
            p318 real NULL
            )
            """
        )
