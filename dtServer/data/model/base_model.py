from peewee import Model 
from dtServer.data.conn import db_proxy
from playhouse.shortcuts import model_to_dict

class BaseModel(Model) : 

    class Meta : 
        database = db_proxy

def model_to_dict_or_none(model) : 
    if model == None : 
        return None
    return model_to_dict(model)