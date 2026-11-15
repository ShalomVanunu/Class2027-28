import sqlite3

db_file = "Our_data.db"

def Read_from_db(sql,file_db):
    connectionDB = sqlite3.connect(file_db)
    cursor = connectionDB.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connectionDB.commit()
    connectionDB.close()
    return data

sql = "SELECT * FROM employee_records"

data = Read_from_db(sql,db_file)
for line in data :
    print(line)
