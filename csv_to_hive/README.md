```shell script
shell启动
root@d9bb2453ce32:/opt/modules/hive-2.3.4-bin# bin/hive
hive> show databases;
hive> use default;
hive (default)> CREATE TABLE 500w (id int,y int,x0 int,x1 int,x2 int, x3 int, x4 int, x5 int, x6 int, x7 int, x8 int, x9 int) ROW FORMAT delimited FIELDS TERMINATED BY ',';
hive (default)> show tables;
hive (default)> desc 500w;
OK
col_name	data_type	comment
id                  	int                 	                    
y                   	int                 	                    
x0                  	int                 	                    
x1                  	int                 	                    
x2                  	int                 	                    
x3                  	int                 	                    
x4                  	int                 	                    
x5                  	int                 	                    
x6                  	int                 	                    
x7                  	int                 	                    
x8                  	int                 	                    
x9                  	int                 	                    
Time taken: 0.063 seconds, Fetched: 12 row(s)
hive (default)> alter table 500w set TBLPROPERTIES ('skip.header.line.count'='1');
#hive (default)> load data local inpath '/opt/modules/datas/test.csv' into table 500w;
hive (default)> load data local inpath '/opt/modules/datas/500w.csv' into table 500w;
hive (default)> select * from 500w limit 10;
hive (default)> select count(*) from 500w;
```