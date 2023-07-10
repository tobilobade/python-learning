
#Create

import pyodbc
try:
    conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes'
    con=pyodbc.connect(conn_string)

    cursor=con.cursor()

    cursor.execute('create table Training.dbo.newEmployee(eno int, ename varchar(20), esalary decimal(10,2),eaddress varchar(10)) ')
    print("table created successfully")
    con.commit() # important when running dml commands

except pyodbc.Error as a:
     if con:
        con.rollback()
        print (a)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()