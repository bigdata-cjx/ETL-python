```shell script
mysql> create database test;
Query OK, 1 row affected (0.00 sec)

mysql> use test;
Database changed

mysql> create table if not exists 500w (id int, y int, x0 int, x1 int, x2 int, x3 int, x4 int, x5 int, x6 int, x7 int, x8 int, x9 int);
Query OK, 0 rows affected (0.01 sec)

mysql> LOAD DATA LOCAL INFILE '/500w.csv' REPLACE INTO TABLE 500w CHARACTER SET UTF8 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;
Query OK, 5000000 rows affected (20.43 sec)
Records: 5000000  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select count(*) from 500w;
+----------+
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (2.32 sec)
```