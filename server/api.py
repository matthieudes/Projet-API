from fastapi import FastAPI

import sqlite3

app = FastAPI()


@app.get("/")
def read_root():
    conn= sqlite3.connect("chinook.db")

    cursor=conn.cursor()
    cursor.execute("Select * From tracks")
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"résultat de recherche ": result}