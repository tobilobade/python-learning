

#UPDATE

import pyodbc

conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes'
conn=pyodbc.connect(conn_string)

cur=conn.cursor()

id=input("Enter ID: ")
name=input("Enter Name: ")

cur.execute('update Training.dbo.S set name=? where id=?',(name,id))

cur.commit() # important when running dml commands

conn.close()