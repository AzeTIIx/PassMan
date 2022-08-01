import sqlite3
def create():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tableAccount(id INTEGER PRIMARY KEY,username TEXT, password TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount")
    rows = cur.fetchall()
    con.close()
    return rows

def search(username="", password=""):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount WHERE username=? or password=?", (username, password))
    rows = cur.fetchall()
    con.close()
    return rows
def add(username,password):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tableAccount VALUES(NULL,?,?,?,?,?,?)", (username, password))
    con.commit()
    con.close()
def update(id, username, password):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("UPDATE tableAccount SET username=?,password=? WHERE id=?", (username, password, id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("accountdb.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tableAccount WHERE id=?",(id,))
    con.commit()
    con.close()
create()

