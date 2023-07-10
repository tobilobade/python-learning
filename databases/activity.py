
import pyodbc

conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes'
conn=pyodbc.connect(conn_string)

cur=conn.cursor()


create_teacher_table = "create table Student(name  VARCHAR(30) PRIMARY KEY, mark INT NOT NULL,course_code varchar(10),Grade varchar(3),employment VARCHAR(30),)"

records = []
# input_amount=int(input("how many input do you want to enter?: "))

# for i in range(0,input_amount):
#     name=input("Enter name: ")
#     mark=int(input("Enter mark: "))
#     course_code=input("Enter course code: ")


#     grade="F"
#     if ( mark>=75 ):
#         grade="A"
#     elif ( mark>65 and mark<=75 ):
#         grade="B"
#     elif ( mark >=55 and mark <=65):
#         grade="C"


#     employment_status="probation"
#     if (grade=="A"):
#         employment_status="have automatic employment"
#     elif (grade=="B" or grade=="C"):
#         employment_status="Open to work"

#     records.append((name,mark,course_code,  grade, employment_status))




# create_values="insert into Student (name,mark,course_code,grade,employment) values(?,?,?,?,?)"

display_probation="select * from student where employment='probation'"

# cur.execute(create_teacher_table)
# cur.executemany(create_values, records)
rows=cur.execute(display_probation)

for row in rows:
    print(row)

cur.commit() # important when running dml commands

conn.close()