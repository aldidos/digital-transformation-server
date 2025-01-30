from peewee import Model, DatabaseProxy
from dtServer.data.conn import db_proxy

class BaseModel(Model) : 

    class Meta : 
        database = db_proxy