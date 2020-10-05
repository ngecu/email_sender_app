import sqlite3

def connect():
    conn=sqlite3.connect("email.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS email (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,email_address text,subject text,message text,time text)")
    conn.commit()
    conn.close()

def insert(email_address,subject,message,time):
    conn=sqlite3.connect("email.db")
    cur=conn.cursor()     
    cur.execute("INSERT INTO email VALUES (NULL,?,?,?,?)",(email_address,subject,message,time))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("email.db")
    cur=conn.cursor()     
    cur.execute("SELECT * FROM email")
    rows=cur.fetchall()
    conn.close() 
    return rows      

def search(email_address="",subject="",message=""):
    conn=sqlite3.connect("email.db")
    cur=conn.cursor()     
    cur.execute("SELECT * FROM email WHERE email_address=? OR subject=? OR message=?",(email_address,subject,message))
    rows=cur.fetchall()
    conn.close() 
    return rows        
 
               
connect()
