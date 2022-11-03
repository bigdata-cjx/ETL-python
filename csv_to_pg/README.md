```shell script
postgres=# CREATE DATABASE test;
CREATE DATABASE
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 dbname    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 test      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(5 rows)

postgres=# \c test
You are now connected to database "test" as user "postgres".
test=# create table if not exists t_500w (id int, y int, x0 int, x1 int, x2 int, x3 int, x4 int, x5 int, x6 int, x7 int, x8 int, x9 int);
CREATE TABLE

test=# \d
         List of relations
 Schema |  Name  | Type  |  Owner   
--------+--------+-------+----------
 public | t_500w | table | postgres
(1 row)

test=# \copy t_500w from '/test.csv' with csv header delimiter ',' encoding 'UTF8';
COPY 9
test=# select count(*) from t_500w;
 count 
-------
     9
(1 row)

test=# TRUNCATE TABLE t_500w;
TRUNCATE TABLE

test=# \copy t_500w from '/500w.csv' with csv header delimiter ',' encoding 'UTF8';
COPY 5000000
test=# select count(*) from t_500w;
  count  
---------
 5000000
(1 row)
```