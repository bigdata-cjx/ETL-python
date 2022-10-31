import json

import pymongo

import time
import pandas as pd

csv_path = "/home/cjx/文档/data-set/fate/500w.csv"


class MongoDBConnect:
    def __init__(self):
        self.host = "192.168.122.251"
        self.port = 27017
        self.db_name = "klb"
        self.db_user = "mongouser"
        self.db_password = "mongopswd"
        self.db_table_name = "500w"

    def get_mongodb_connect(self):
        host = self.host
        port = self.port
        user = self.db_user
        password = self.db_password
        database = self.db_name
        client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")
        db = client[database]
        return db

    def insert_to_mongodb(self):
        data = pd.read_csv(csv_path)
        data = json.loads(data.to_json(orient="records"))
        mongodb_client = self.get_mongodb_connect()
        mongodb_client[self.db_table_name].insert_many(data)

    def get_row_num(self):
        count = self.get_mongodb_connect()[self.db_table_name].count_documents({})
        return count

    def drop_collection(self):
        self.get_mongodb_connect()[self.db_table_name].drop()

    def read_from_db(self):
        mongodb_client = self.get_mongodb_connect()
        result = (
            mongodb_client[self.db_table_name].find({}, {"_id": 0}).limit(10).skip(0)
        )
        return result


if __name__ == "__main__":
    start = time.perf_counter()
    mongodb_connect = MongoDBConnect()
    # mongodb_connect.drop_collection()
    # mongodb_connect.insert_to_mongodb()
    # print(mongodb_connect.get_row_num())
    for i in mongodb_connect.read_from_db():
        print(i)
    print("cost %s second" % (time.perf_counter() - start))
