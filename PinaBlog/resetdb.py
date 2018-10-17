import sqlite3
import csv

DB_FILE="blogger.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def resetTable():
    try:
        c.execute("DROP TABLE login")
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("INSERT INTO login VALUES('john', 'doe')")
        c.execute("INSERT INTO login VALUES('jane', 'doe')")
    except:
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("INSERT INTO login VALUES('john', 'doe')")
        c.execute("INSERT INTO login VALUES('jane', 'doe')")
        
def readFrom():
    c.execute("SELECT * FROM login")
    print(c.fetchall())

resetTable()
readFrom()
    
db.commit()
db.close()
