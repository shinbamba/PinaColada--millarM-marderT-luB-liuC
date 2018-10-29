import sqlite3
import csv

DB_FILE="blogger.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

def resetTable():
    try:
        c.execute("DROP TABLE login")
        c.execute("DROP TABLE post")
        c.execute("DROP TABLE blog")
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("CREATE TABLE blog(username TEXT, category TEXT, blog_title TEXT, description TEXT, blog_id INTEGER)")
        c.execute("CREATE TABLE post(username TEXT, post_title TEXT, body TEXT, blog_id INTEGER, post_id INTEGER, timestamp DATETIME)")
        c.execute("INSERT INTO login VALUES('John', 'Doe')")
        c.execute("INSERT INTO login VALUES('Jane', 'Doe')")
        c.execute("INSERT INTO blog VALUES('John', 'Sports', 'Test Blog', 'TEST BLOG', 1)")
        c.execute("INSERT INTO blog VALUES('Jane', 'Fashion', 'Other Test Blog', 'TEST BLOG', 1)")
        c.execute("INSERT INTO post VALUES('John', 'Test Post', 'TEST POST', 1, 1, CURRENT_TIMESTAMP)")
        c.execute("INSERT INTO post VALUES('Jane', 'Other Test Post', 'TEST POST', 1, 1, CURRENT_TIMESTAMP)")
    except:
        c.execute("CREATE TABLE login(username TEXT, password TEXT)")
        c.execute("CREATE TABLE blog(username TEXT, category TEXT, blog_title TEXT, description TEXT, blog_id INTEGER)")
        c.execute("CREATE TABLE post(username TEXT, post_title TEXT, body TEXT, blog_id INTEGER, post_id INTEGER, timestamp DATETIME)")
        c.execute("INSERT INTO login VALUES('John', 'Doe')")
        c.execute("INSERT INTO login VALUES('jane', 'Doe')")
        c.execute("INSERT INTO blog VALUES('John', 'Sports', 'Test Blog', 'TEST BLOG', 1)")
        c.execute("INSERT INTO blog VALUES('Jane', 'Fashion', 'Other Test Blog', 'TEST BLOG', 1)")
        c.execute("INSERT INTO post VALUES('John', 'Test Post', 'TEST POST', 1, 1, CURRENT_TIMESTAMP)")
        c.execute("INSERT INTO post VALUES('Jane', 'Other Test Post', 'TEST POST', 1, 1, CURRENT_TIMESTAMP)")
        
def readFrom():
    c.execute("SELECT * FROM login")
    print(c.fetchall())
    c.execute("SELECT * FROM blog")
    print(c.fetchall())
    c.execute("SELECT * FROM post")
    print(c.fetchall())

resetTable()
readFrom()
    
db.commit()
db.close()
