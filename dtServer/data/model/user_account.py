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

def save_user_account(data : dict ) -> UserAccount :
    model = dict_to_model(UserAccount, data)
    model.save()
    return model_to_dict(model)

def get_user_account_by_loginid(login_id : str) -> UserAccount : 
    user_account = UserAccount.get_or_none(UserAccount.login_id == login_id)
    return model_to_dict_or_none(user_account)

def insert_user_accounts(list_data) : 
    with db_proxy.atomic() : 
        UserAccount.insert_many(list_data).execute()