import time

import pandas as pd
import psycopg2
import psycopg2.extras

csv_path = "/home/cjx/文档/data-set/fate/500w.csv"
test_csv_path = "ETL-python/csv_operation/test.csv"


class pgConnect:
    def __init__(self):
        self.host = "192.168.122.251"
        self.port = 5432
        self.db_name = "dbname"
        self.db_user = "postgres"
        self.db_password = "123456"
        self.db_table_name = "500w"

    def get_pg_connect(self):
        conn = psycopg2.connect(
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.host,
            port=self.port,
        )
        return conn

    def create_table(self):
        # 编写sql，create_sql负责创建表
        create_sql = f"""CREATE TABLE {self.db_table_name} (id int,y int,x0 int,x1 int,x2 int, x3 int, x4 int, x5 int, x6 int, x7 int, x8 int, x9 int)"""
        # 使用数据库
        conn = self.get_pg_connect()
        cur = conn.cursor()
        cur.execute("use %s" % self.db_name)
        # 执行create_sql，创建表
        cur.execute(create_sql)
        conn.commit()
        # 关闭连接
        conn.close()
        cur.close()

    def insert_to_pg(self):
        self.create_table()
        conn = self.get_pg_connect()
        cur = conn.cursor()
        with open(test_csv_path, 'r', encoding='utf-8') as f:
            # 跳过表头
            next(f)
            cur.copy_from(f, self.db_table_name, sep=',', )
        conn.commit()

    def get_row_num(self):
        conn = self.get_pg_connect()
        cur = conn.cursor()
        cur.execute(f"select count(*) from {self.db_name}.{self.db_table_name};")
        # 关闭连接
        conn.close()
        cur.close()
        return cur.fetchone()

    def drop_table(self):
        conn = self.get_pg_connect()
        cur = conn.cursor()
        cur.execute(f"drop table if exists {self.db_name}.{self.db_table_name};")
        # 关闭连接
        conn.close()
        cur.close()

    def read_from_db(self):
        conn = self.get_pg_connect()
        cur = conn.cursor()
        cur.execute(f"select * from {self.db_name}.{self.db_table_name} limit 10;")
        conn.commit()
        # 关闭连接
        conn.close()
        cur.close()
        print(cur.fetchone())


if __name__ == "__main__":
    start = time.perf_counter()
    pg_connect = pgConnect()
    pg_connect.drop_table()
    pg_connect.insert_to_pg()
    print(pg_connect.get_row_num())
    pg_connect.read_from_db()
    print("cost %s second" % (time.perf_counter() - start))
