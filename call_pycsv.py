import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import time
import calendar
import os
import sys
import pro
#sys.path.extend(['/home/maninsuit/work/projects/xsg/csvp/'])
#from pathlib import Path
path = os.getcwd()
# 默认csv文件在当前目录下，后续可根据实际情况修改
#path = '\test\test\csvfiles'
table_list = []

#for fn in os.listdir(path):
#    if fn.endswith('.csv'):
#        table_list.append(file)
#data = pd.read_csv(table_list,sep="|", names=col)
new_table_list = []

for fn in os.listdir(path):
    if fn.endswith('.csv'):
        table_list.append(pd.read_csv(fn,sep="|"))
        new_table_list.append(fn.split(".")[0])
ts = calendar.timegm(time.gmtime())
for item in new_table_list:
    tn = item + str(ts)
    # can't work properly due to virtualenv
#    sout, ttt = subprocess.check_output([sys.executable, "pro.py", "ZJJKFINANCINGANALYZE"])
#    print("这个是sout: ",sout)
#    strs = ('python3 pro.py ZJJKFINANCINGANALYZE')
#    p = os.system(strs)
#    print("这是: ",p)
    tts,ttt = pro.search(item)
    values = '%s'
    n = 1
    #for k in range(1, ttt,1):
    while n < ttt:
        values = values + ',%s' 
        n = n + 1
    tnf = item + ".csv"
    emp = pd.read_csv(tnf, index_col=False, delimiter=',')
    emp.head()
    try:
        conn = msql.connect(host='172.20.4.28', user='test',
                            password='asd.1234',database='BI') 
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            sqlz = "DROP TABLE IF EXISTS " + tn + ";"
            cursor.execute(sqlz)
            # 目前无法自动读取格式，需手动录入
            sqts = "CREATE TABLE " + tn + "(" + tts
            sqlx = "CREATE TABLE " + tn + "(ORG_ID bigint,JRJG varchar(200),RZCBL varchar(200))" +";"
            #print("this is executed: ",sqlx)
            cursor.execute(sqts)
            for i,row in emp.iterrows():
                sql = "INSERT INTO " + tn + " VALUES" + " (" + values+ ")"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                conn.commit()
    except Error as e:
        print("Error while connecting to MySQL",e)
