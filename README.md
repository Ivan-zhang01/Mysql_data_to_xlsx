# Mysql_data_to_xlsx
Using python3, export mysql table data to xlsx, you can put your query in sql file as a parameter

The usage as below:
python3 exports.py <mysql_host> <db_user> <db_name>


1. Put your query in test.sql as:
select * from users;

2.execute above command:
python3 exports.py <mysql_host> <db_user> <db_name>

Note:It's pending for you to enter db_password.

3.check the output file then

---------------------------------------------------
This script is too simple, you should modify it once using it
