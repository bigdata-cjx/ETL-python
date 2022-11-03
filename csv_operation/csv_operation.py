import time

import pandas as pd

csv_path = "/home/cjx/文档/data-set/fate/500w.csv"


def head_data(num: int):
    head = pd.read_csv(csv_path, engine="python", nrows=num)
    print(head)  # 打印前 n 行
    """
       id  y  x0  x1  x2  x3  x4  x5  x6  x7  x8  x9
    0   0  1  60  24  62  94  59  53   5  13  10  76
    1   1  0  88  19   4  38   7  73  51  88  58   2
    2   2  1  56  23  14  33   1   9  73  68  61  38
    3   3  1  78  71  39  48  84  45  76  89  55  81
    4   4  1  74  28  58  62  59  35  63  98  28  26
    """


def get_data():
    # 用pandas读取csv
    # data = pd.read_csv(file_name,engine='python',encoding='gbk')
    data = pd.read_csv(csv_path, engine="python")
    # print(data.head(5))  # 打印前5行


if __name__ == "__main__":
    start = time.perf_counter()
    head_data(5)
    # get_data()
    print("cost %s second" % (time.perf_counter() - start))
