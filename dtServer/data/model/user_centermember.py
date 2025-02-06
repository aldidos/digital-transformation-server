from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.center_member import CenterMember

class UserCenterMember(BaseModel) : 
    user = ForeignKeyField(User, unique = True)
    centermember = ForeignKeyField(CenterMember, unique = True)

    class Meta : 
        table_name = 'user_centermember'

