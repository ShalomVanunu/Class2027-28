import sqlite3

db_file = "Our_data.db"


def run_sql(SQL,db_file):
    connection = sqlite3.connect(db_file) #connect to db file
    cursor = connection.cursor() # first line in db
    cursor.execute(SQL) # do the sql command
    connection.commit() #act / do

sql = "INSERT INTO employee_records VALUES (1,'shalom', 'software', 5)"
run_sql(sql,db_file)