#from ssl import _PasswordType
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import time
import calendar
import os
#from pathlib import Path
#empdata = pd.read_csv('ZJJKFINANCINGCBL.csv', index_col=False, delimiter = ',')
#empdata.head()
path = os.getcwd()
# 默认csv文件在当前目录下，后续可根据实际情况修改
#path = '\test\test\csvfiles'
table_list = []

#for fn in os.listdir(path):
#    if fn.endswith('.csv'):
#        table_list.append(file)
#data = pd.read_csv(table_list,sep="|", names=col)
new_table_list = []
def search(args):
    with open('sql.txt', 'r') as f:
        c=0
        a = []
        for l in f.readlines():
            l = l.strip()
            c+=1
            if l == "":
                a.append(c)
        step = 2
        list__ = [a[i:i+step] for i in range(0, len(a)-1, 1)]
        for ii in list__:
            ii[0] = ii[0] + 1
            ii[1] = ii[1] - 1
            f.seek(0)
            temp = f.read().splitlines()
            for x in temp[ii[0]:ii[1]]:
                if args in x:
                    fi = temp[ii[0]+1:ii[1]]
                    s = ii[1] - ii[0] - 2
                    #print("行数为： ",s)
                    string = ' '.join([str(item) for item in fi])
                    new = (string, s) 
                    return(new)
#                    return(temp[ii[0]+1:ii[1]])

for fn in os.listdir(path):
    if fn.endswith('.csv'):
        table_list.append(pd.read_csv(fn,sep="|"))
        new_table_list.append(fn.split(".")[0])
        #print("the table list: ",new_table_list)
#for fn in os.listdir(.):
#    if fn.endswith('.csv'):
#        table_list.append(pd.read_csv(fn, sep="|"))
#        new
# 读取csv文件并输出,增加扩展性
#with open('ZJJKFINANCINGCBL.csv', 'w', newline='') as csvfile:
#    spamreader = csv.reader(scvfile, delimiter=' ', quotechar="|")
#    for row in spamreader:
#        print(', '.join(row))
ts = calendar.timegm(time.gmtime())
for item in new_table_list:
    tn = item + str(ts)
    tts,ttt = search(item)
    values = '%s'
   # for k in range(1, ttt,1):
    n = 1
    while n < ttt:
        values = values + ',%s' 
        n = n + 1
    tnf = item + ".csv"
    emp = pd.read_csv(tnf, index_col=False, delimiter=',')
    emp.head()
    try:
        conn = msql.connect(host='172.20.4.28', user='test',
                            password='asd.1234',database='BI') 
    # password 
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
