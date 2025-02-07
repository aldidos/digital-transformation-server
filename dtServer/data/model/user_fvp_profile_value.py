from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.user_fvp_profile import UserFVPProfile
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserFVPProfileValue(BaseModel) : 
    user_fvp_profile = ForeignKeyField(UserFVPProfile) 
    weight = FloatField()
    mean_velocity = FloatField()
    mean_power = FloatField()
    
    class Meta : 
        table_name = 'user_fvp_profile_value'