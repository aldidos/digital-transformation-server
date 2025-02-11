from peewee import Model 
from dtServer.data.conn import db_proxy
from playhouse.shortcuts import model_to_dict

DATE_FORMAT = '%y-%m-%d'
DATETIME_FORMAT = '%y-%m-%d %H:%M:%S'
TIME_FORMAT = '%H:%M:%S'

class BaseModel(Model) : 

    class Meta : 
        database = db_proxy

def model_to_dict_or_none(model) : 
    if model == None : 
        return None
    return model_to_dict(model)