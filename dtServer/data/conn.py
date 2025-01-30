from peewee import *
from dotenv import load_dotenv
import os

db_proxy = DatabaseProxy()

def init_db_conn() : 
    conn = make_database_connection()    
    print()

def create_connection(db, user, password, host, port) : 
    conn = MySQLDatabase(db, user = user, password = password, host = host, port=port)    
    conn.connect()
    return conn

def make_database_connection() -> MySQLDatabase : 
    load_dotenv()
    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT'))
    db = os.environ.get('DATABASE')

    return create_connection(db, user, password, host, port)

