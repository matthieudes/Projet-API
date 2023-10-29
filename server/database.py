from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models
import sqlite3

def create_connection(database_file):
    connection = None
    try :
        connection = sqlite3.connect(database_file)
        print(f"Connexion à la base de données{database_file} établie.")
        return connection
    except sqlite3.Error as e:
        print(f"Erreur lors de la connection à la base de données :{e}")
        if connection:
            connection.close()

if __name__=='__api__':
    database_file='.chinook.db'
    connection = create_connection(database_file)



db_url="sqlite:///./chinook.db"