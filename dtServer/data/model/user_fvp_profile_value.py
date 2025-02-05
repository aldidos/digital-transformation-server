from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none, db_proxy
from dtServer.data.model.user_fvp_profile import UserFVPProfile
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserFVPProfileValue(BaseModel) : 
    user_fvp_profile = ForeignKeyField(UserFVPProfile) 
    weight = FloatField()
    mean_velocity = FloatField()
    mean_power = FloatField()
    
    class Meta : 
        table_name = 'user_fvp_profile_data'

def save_workout(data : dict) : 
    model = dict_to_model(UserFVPProfileValue, data)
    model.save()
    return model_to_dict(model)

def insert_many_user_fvp_profile_data(list_data) : 
    with db_proxy.atomic() : 
        UserFVPProfileValue.insert_many(list_data).execute()

def select_user_fvp_profile_data(user_fvp_profile_id) : 
    q = UserFVPProfileValue.select().where(UserFVPProfileValue.user_fvp_profile_id == user_fvp_profile_id)
    list_data = [ model_to_dict(row) for row in q ]
    return list_data