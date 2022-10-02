import mysql.connector

conn=mysql.connector.connect(host="localhost",database="spring_security_custom_user_demo",user="root",password="root")
if conn.is_connected():
    print("connected...... ")

cursor=conn.cursor()
cursor.execute("select * from user")
row=cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

rows=cursor.fetchall()
print("Total number of rows ",cursor.rowcount)
for row1 in rows:
    print(row1)

cursor.close()
