from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_account import UserAccount, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserAccountDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserAccount, data) )
    
    def get_by_loginid(self, login_id : str) -> UserAccount : 
        user_account = UserAccount.get_or_none(UserAccount.login_id == login_id)
        return model_to_dict_or_none(user_account)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            UserAccount.insert_many(list_data).execute()

userAccountDao = UserAccountDao()