#standard steps for creating db
#import database specific module
#establish a connection towards the db with credentials n a secured way
#create a cursor object
#use in built methods to execute the sql queries
#commit or rollback
#fetch the result from cursor
#close the resources

#"Driver= 0DBC Driver 17 for SQL Serber; SERVER=ISW-MKT-AO1\SQLEXPRESS;DATABASE=Training;Tusted_connection=yes;"

import pyodbc

conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes'
conn=pyodbc.connect(conn_string)

cur=conn.cursor()

cur.execute("SELECT * FROM Training.dbo.S")

for row in cur:
    print(row)

conn.close()

