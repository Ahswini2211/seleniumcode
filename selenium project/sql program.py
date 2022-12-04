import mysql.connector

conn = mysql.connector.connect(host ='localhost', database = 'apidevelop', username = 'root', password = 'ASH@2211#ni')

cursor = conn.cursor()

print(conn.is_connected())

mysql = "select * from CustomerInfo"

cursor.execute(mysql)

row = cursor.fetchall()

print(type(row))

print(row)