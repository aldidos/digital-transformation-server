from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenter(BaseModel) : 
    user = ForeignKeyField(User)
    center = ForeignKeyField(Center)

    class Meta : 
        table_name = 'user_center'

