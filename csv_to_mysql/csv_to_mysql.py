import time

import pandas as pd
import pymysql

csv_path = "/home/cjx/文档/data-set/fate/500w.csv"


class MySQLConnect:
    def __init__(self):
        self.host = "192.168.122.251"
        self.port = 3307
        self.db_name = "test"
        self.db_user = "root"
        self.db_password = "123456"
        self.db_table_name = "500w"

    def get_mysql_connect(self):
        conn = pymysql.connect(
            user=self.db_user,
            passwd=self.db_password,
            db=self.db_name,
            host=self.host,
            port=self.port,
            charset="utf8mb4",
            local_infile=1,
        )
        return conn

    def create_table(self):
        # 打开csv文件
        file = open(csv_path, "r", encoding="utf-8")
        # 读取csv文件第一行字段名，创建表
        reader = file.readline()
        b = reader.split(",")
        field = ""
        for a in b:
            field = field + a + " int,"
        field = field[:-1]
        # 编写sql，create_sql负责创建表，data_sql负责导入数据
        create_sql = f"create table if not exists {self.db_table_name} ({field}) DEFAULT CHARSET=utf8"
        # 使用数据库
        conn = self.get_mysql_connect()
        cur = conn.cursor()
        cur.execute("use %s" % self.db_name)
        # 设置编码格式
        cur.execute("SET NAMES utf8;")
        cur.execute("SET character_set_connection=utf8;")
        cur.execute("set global local_infile=on;")
        # 执行create_sql，创建表
        cur.execute(create_sql)
        conn.commit()
        # 关闭连接
        conn.close()
        cur.close()

    def insert_to_mysql_load_data(self):
        self.create_table()
        data_sql = f"LOAD DATA LOCAL INFILE '{csv_path}' REPLACE INTO TABLE {self.db_name}.{self.db_table_name} CHARACTER SET UTF8 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES;"
        print(data_sql)
        conn = self.get_mysql_connect()
        cur = conn.cursor()
        # 执行data_sql，导入数据
        cur.execute(data_sql)
        conn.commit()
        # 关闭连接
        conn.close()
        cur.close()

    def insert_to_mysql(self):
        self.create_table()
        # 用pandas读取csv
        # data = pd.read_csv(file_name,engine='python',encoding='gbk')
        # data = pd.read_csv(csv_path, engine="python", nrows=10)
        data = pd.read_csv(csv_path, engine="python")
        conn = self.get_mysql_connect()
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        # 数据过滤，替换 nan 值为 None
        # data = data.astype(object).where(pd.notnull(data), None)

        # 写入数据 id  y  x0  x1  x2  x3  x4  x5  x6  x7  x8  x9
        for id, y, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 in zip(
            data["id"],
            data["y"],
            data["x0"],
            data["x1"],
            data["x2"],
            data["x3"],
            data["x4"],
            data["x5"],
            data["x6"],
            data["x7"],
            data["x8"],
            data["x9"],
        ):
            try:
                insertsql = f"INSERT INTO {self.db_table_name}(id, y, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9) VALUES({id},{y},{x0},{x1},{x2},{x3},{x4},{x5},{x6},{x7},{x8},{x9})"
                # insertsql = f"INSERT INTO {self.db_table_name}(id, y, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9) VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"
                cursor.execute(insertsql)
                # cursor.execute(insertsql, dataList)
                conn.commit()
            except Exception as e:
                print("Exception")
                print(e)
                conn.rollback()
            # time.sleep(3)

        cursor.close()
        # 关闭数据库连接
        conn.close()

    def get_row_num(self):
        conn = self.get_mysql_connect()
        cur = conn.cursor()
        cur.execute(f"select count(*) from {self.db_name}.{self.db_table_name};")
        # 关闭连接
        conn.close()
        cur.close()
        return cur.fetchone()

    def drop_table(self):
        conn = self.get_mysql_connect()
        cur = conn.cursor()
        cur.execute(f"drop table if exists {self.db_name}.{self.db_table_name};")
        # 关闭连接
        conn.close()
        cur.close()

    def read_from_db(self):
        conn = self.get_mysql_connect()
        cur = conn.cursor()
        cur.execute(
            f"select * from {self.db_name}.{self.db_table_name} limit 10;"
        )
        conn.commit()
        # 关闭连接
        conn.close()
        cur.close()
        print(cur.fetchone())


if __name__ == "__main__":
    start = time.perf_counter()
    mysql_connect = MySQLConnect()
    mysql_connect.drop_table()
    mysql_connect.insert_to_mysql()
    print(mysql_connect.get_row_num())
    mysql_connect.read_from_db()
    print("cost %s second" % (time.perf_counter() - start))
