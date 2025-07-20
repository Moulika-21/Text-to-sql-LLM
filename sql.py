import sqlite3

connection=sqlite3.connect("student.db") #connect to sqlite

#create a  cursor object to insert record,create table,retrieve
cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""
## to execute the the table in cursor 
cursor.execute(table_info)

#insert records
cursor.execute('''Insert Into STUDENT values('Deepika','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Advaith','Machine Learning','B',100)''')
cursor.execute('''Insert Into STUDENT values('Pragnya','Data Science','A',70)''')
cursor.execute('''Insert Into STUDENT values('Nihan','Data Science','A',60)''')
cursor.execute('''Insert Into STUDENT values('Pranuthi','Machine Learning','B',35)''')

##Display all the records
print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

##close the connection
connection.commit()
connection.close()