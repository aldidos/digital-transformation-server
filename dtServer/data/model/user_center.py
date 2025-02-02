from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenter(BaseModel) : 
    user_id = ForeignKeyField(User)
    center_id = ForeignKeyField(Center)

    class Meta : 
        table_name = 'user_center'

def create_user_center(user_id, center_id) : 
    data = {
        'user_id' : user_id, 
        'center_id' : center_id
    }
    return save_user_center(data)

def save_user_center(data : dict) :
    model = dict_to_model(UserCenter, data)
    model.save()
    return model_to_dict(model)

def get_user_centers(user_id : int) : 
    q = UserCenter.select().where(UserCenter.user_id == user_id)
    list_data = [model_to_dict(row) for row in q]
    return list_data

def get_user_center(user_id : int, center_id : int) : 
    model =  UserCenter.get_or_none(UserCenter.user_id == user_id and UserCenter.center_id == center_id)
    return model_to_dict_or_none(model)

def insert_user_center(list_data) : 
    with db_proxy.atomic() :
        UserCenter.insert_many(list_data).execute()