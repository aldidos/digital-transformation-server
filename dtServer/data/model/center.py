from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_ADDRESS = 512

class Center(BaseModel) : 
    name = CharField(LEN_NAME, index = True)
    address = CharField(LEN_ADDRESS, index = True) 
    
    class Meta : 
        table_name = 'center'

