from peewee import *
from dotenv import load_dotenv
import os

db_proxy = DatabaseProxy()

def init_db_conn() : 
    conn = make_database_connection()    

def create_connection(db, user, password, host, port) : 
    conn = MySQLDatabase(db, user = user, password = password, host = host, port=port)    
    conn.connect()
    return conn

def make_database_connection() -> MySQLDatabase : 
    load_dotenv()
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    db = os.getenv('DATABASE')

    return create_connection(db, user, password, host, port)

