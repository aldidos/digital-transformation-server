from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenter(BaseModel) : 
    user_id = ForeignKeyField(User)
    center_id = ForeignKeyField(Center)

    class Meta : 
        table_name = 'user_center'


def save_user_center(data : dict) :
    model = dict_to_model(UserCenter, data)
    model.save()
    return model_to_dict(model)

def get_user_centers(user_id : int) : 
    q = UserCenter.select().where(UserCenter.user_id == user_id)
    list_data = [model_to_dict(row) for row in q]
    return list_data

def get_user_center(user_id : int, center_id : int) : 
    data_model = UserCenter.select().where(UserCenter.user_id == user_id and UserCenter.center_id == center_id).get()
    return model_to_dict(data_model)