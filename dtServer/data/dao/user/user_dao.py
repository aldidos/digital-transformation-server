from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.base_model import db_proxy, model_to_dict_or_none
from dtServer.data.model.user.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(User, data) )
    
    def select_by_id(self, id : int) :
        user = User.get_or_none( User.id == id )
        return model_to_dict_or_none(user)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            User.insert_many(list_data).execute()

userDao = UserDao()