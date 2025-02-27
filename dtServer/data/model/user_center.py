from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.user.user import User
from dtServer.data.model.center.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenter(BaseModel) : 
    user = ForeignKeyField(User, index = True)
    center = ForeignKeyField(Center, index = True)

    class Meta : 
        table_name = 'user_center'

