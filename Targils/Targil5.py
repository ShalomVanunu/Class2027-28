import sqlite3

db = 'carData.db'
sql3 = """CREATE TABLE IF NOT EXISTS cars (
Id INTEGER,
[car Name] TEXT,
[Mount of production] INTEGER,
[Mount of Sells] INTEGER
)"""


file = 'cars.md'
def read_file(file):
    with open(file, 'r') as f:
        return f.read()





def create_db(sql,db):
    connection = sqlite3.connect(db)  # connect to db file
    cursor = connection.cursor()  # first line in db
    cursor.execute(sql)  # do the sql command
    connection.commit()  # act / do

def main(file, db):
    create_db(sql3, db)
    txt = read_file(file)

    txt= txt.split("\n")
    txt = txt[2:-1]
    for line in txt:
        id=line.split("|")[1].strip()
        name=line.split("|")[2].strip()
        prod=line.split("|")[3].strip()
        sells=line.split("|")[4].strip() #lior shapira maflitz
        sql=f"INSERT INTO cars VALUES({id},'{name}',{prod},{sells})"
        create_db(sql,db)

main(file,db)






