import sys
sys.path.append('./')
from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_ID = 128
LEN_PW = 128

class UserAccount(BaseModel) : 
    login_id = CharField(LEN_ID, unique = True)
    login_pw = CharField(LEN_PW, index = True)
    user_id = ForeignKeyField(User) ####

    class Meta : 
        table_name = 'user_account'

def save_user_account(data : dict ) -> UserAccount :
    model = dict_to_model(UserAccount, data)
    model.save()
    return model_to_dict(model)

def get_user_account_by_loginid(login_id : str) -> UserAccount : 
    try : 
        model = UserAccount.select().where( UserAccount.login_id == login_id ).get()
        return model_to_dict(model)
    except DoesNotExist : 
        return None