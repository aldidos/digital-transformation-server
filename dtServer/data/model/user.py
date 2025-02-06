from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.util.json_encoder import encode

LEN_ID = 16
LEN_PW = 16
LEN_NAME = 32
LEN_CONTACT = 16
LEN_GENDER = 8
DATE_FORMAT = '%y-%m-%d'

class User(BaseModel) : 
    name = CharField(LEN_NAME,index = True)
    weight = FloatField(False)
    height = FloatField(False)
    birthday = DateField(DATE_FORMAT)
    contact = CharField(LEN_CONTACT)
    gender = CharField(LEN_GENDER) 

    workout_routine = IntegerField(True)
    workout_freq = IntegerField(True)

    class Meta : 
        table_name = 'user'
