import sqlite3

db_file = "students_db.db"

create_table = """ CREATE TABLE students (
id INTEGER,
name TEXT,
l_name TEXT,
age INTEGER)"""

def run_sql(SQL,db_file):
    connection = sqlite3.connect(db_file) #connect to db file
    cursor = connection.cursor() # first line in db
    cursor.execute(SQL) # do the sql command
    connection.commit() #act / do

run_sql(create_table,db_file)

hana_sql = "INSERT INTO students VALUES (1, 'hanna', 'meseri', 16)"

run_sql(hana_sql,db_file)



