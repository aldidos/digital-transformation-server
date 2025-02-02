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

def save_user(data : dict) -> User : 
    user = dict_to_model(User, data)
    user.save()
    return model_to_dict(user)

def select_user_by_id(id : int) :
    user = User.get_or_none( User.id == id )
    return model_to_dict_or_none(user)

def select_users() : 
    query = User.select()
    users = [ model_to_dict(row) for row in query]    
    return users

def insert_users(list_data) : 
    with db_proxy.atomic() : 
        User.insert_many(list_data).execute()