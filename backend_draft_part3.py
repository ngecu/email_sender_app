import sqlite3

def connect():
    conn=sqlite3.connect("draft.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS draft (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,email_address text,subject text,message text,time text)")
    conn.commit()
    conn.close()

def insert(email_address,subject,message,time):
    conn=sqlite3.connect("draft.db")
    cur=conn.cursor()     
    cur.execute("INSERT INTO draft VALUES (NULL,?,?,?,?)",(email_address,subject,message,time))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("draft.db")
    cur=conn.cursor()     
    cur.execute("SELECT * FROM draft")
    rows=cur.fetchall()
    conn.close() 
    return rows      

def search(email_address="",subject="",message=""):
    conn=sqlite3.connect("draft.db")
    cur=conn.cursor()     
    cur.execute("SELECT * FROM draft WHERE email_address=? OR subject=? OR message=?",(email_address,subject,message))
    rows=cur.fetchall()
    conn.close() 
    return rows        

               
connect()
