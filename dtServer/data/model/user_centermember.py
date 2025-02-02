from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.center_member import CenterMember

class User_CenterMember(BaseModel) : 
    user_id = ForeignKeyField(User, unique = True)
    centermember_id = ForeignKeyField(CenterMember, unique = True)

    class Meta : 
        table_name = 'user_centermember'

def create_user_centermember(user_id, centermember_id) : 
    data = {
        "user_id" : user_id, 
        "centermember_id" : centermember_id
    }
    save_user_centermember(data)

def save_user_centermember(data) : 
    model = dict_to_model(User_CenterMember, data)
    model.save()
    return model_to_dict(model)

def select_centermember(user_id) : 
    model = User_CenterMember.get_or_none( User_CenterMember.user_id == user_id )     
    return model_to_dict_or_none(model)

def select_user(centermember_id) : 
    model = User_CenterMember.get_or_none( User_CenterMember.centermember_id == centermember_id ) 
    return model_to_dict_or_none(model)