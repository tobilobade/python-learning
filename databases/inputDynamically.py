
import pyodbc 
try:
    conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes'
    conn=pyodbc.connect(conn_string)

    eno=int(input("Enter Employee Number."))
    ename=input("Enter Employee Name:")
    esal=float(input("Enter Employee Salary:"))
    eaddr=input("Enter Employee Address.")
    sql="insert into Training.dbo.employees values(?, ?, ?, ?)"
    cursor=conn.cursor()

    cursor.execute(sql,(eno, ename, esal, eaddr))
    print("Record Inserted Successfully")
    option=input("Do you want to insert one more record[Yes| No] :")    

    if option=="No":
        conn.commit()
    

except pyodbc.Error as e:
    if conn:
        conn.rollback()
        print(e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()