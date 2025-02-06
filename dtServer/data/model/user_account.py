from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_ID = 128
LEN_PW = 128

class UserAccount(BaseModel) : 
    login_id = CharField(LEN_ID, unique = True)
    login_pw = CharField(LEN_PW, index = True)
    user = ForeignKeyField(User) ####

    class Meta : 
        table_name = 'user_account'
