from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_fvp_profile_value import UserFVPProfileValue, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserFVPProfileValueDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserFVPProfileValue, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            UserFVPProfileValue.insert_many(list_data).execute()

    def select_by_profile_id(self, user_fvp_profile_id) : 
        q = UserFVPProfileValue.select().where(UserFVPProfileValue.user_fvp_profile == user_fvp_profile_id)
        list_data = [ model_to_dict(row) for row in q ]
        return list_data
    
userFVPProfileValueDao = UserFVPProfileValueDao()