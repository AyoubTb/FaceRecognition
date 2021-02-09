import pymysql
from datetime import datetime

connection = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='BD_Perso',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

now = datetime.now()
dtString = now.strftime('%H:%M:%S')
with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `salarie` (`name`, `time`) VALUES (%s, %s)"
        cursor.execute(sql, ("name", dtString))
    connection.commit()