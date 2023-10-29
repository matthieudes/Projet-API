from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from . import models
import sqlite3


def create_connection():
    connection = sqlite3.connect('chinook.db')
    return connection