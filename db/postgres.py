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

    def drop_all_tables(self):
        with open("./db/queries/drop.sql") as f:
            self.cur.execute(f.read())

    def create_db_json(self, restart):
        if restart == True:
            self.drop_all_tables()

        with open("./db/queries/create_json.sql") as f:
            self.cur.execute(f.read())

    def create_db_unified(self, restart):
        if restart == True:
            self.drop_all_tables()

        with open("./db/queries/create_one.sql") as f:
            self.cur.execute(f.read())

    def create_db_3_tables(self, restart):
        if restart:
            self.drop_all_tables()

        with open("./db/queries/create_3.sql") as f:
            self.cur.execute(f.read())
