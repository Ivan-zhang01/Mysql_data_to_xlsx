###############
#
#This script used to export data from mysql database
#the sql used to export is from file
#
###############
import pymysql
import os
import xlsxwriter
import sys
from sys import argv
script,first,second,third=argv
host=sys.argv[1]
user=sys.argv[2]
#pwd=sys.argv[3]
pwd=input()
db=sys.argv[3]
try:
    os.environ['NLS_LANG'] = 'en_US.utf8'
    print(argv[1])
    print(argv[2])
    print(argv[3])
    print(pwd)
    db = pymysql.connect(host, user, pwd, db, charset='utf8')
    c = db.cursor()
    ##读取SQL文件,获得sql语句的list
    with open('test.sql', 'r+') as f:
        sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
        sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
    ##执行sql语句，使用循环执行sql语句
    for sql_item in sql_list:
        ##print(sql_item)
        c.execute(sql_item)
        data = c.fetchall()
        workbook = xlsxwriter.Workbook('file3.xlsx')
        worksheet = workbook.add_worksheet()
        for i in range(len(data)):
            for j in range(len(data[i])):
                worksheet.write(i, j, data[i][j])
        workbook.close()
        #for dd in data:
        #    print(dd)
except pymysql.Error as e:
    print(e)
finally:
    c.close()
    db.commit()
    db.close()
