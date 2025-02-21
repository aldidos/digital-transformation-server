from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.base_model import model_to_dict_or_none
from dtServer.data.model.user_fvp_profile import UserFVPProfile
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserFVPProfileDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserFVPProfile, data) )
    
    def insert(self, data) : 
        return UserFVPProfile.insert(data).execute()
    
    def select_by_user(self, user_id) : 
        q = UserFVPProfile.select().where(UserFVPProfile.user == user_id)
        list_data = [ model_to_dict(row) for row in q ]
        return list_data

    def select_by_user_and_exercise_library(self, user_id, exercise_library_id) : 
        model = UserFVPProfile.get_or_none(UserFVPProfile.user == user_id, UserFVPProfile.exercise_library == exercise_library_id )
        return model_to_dict_or_none(model)
    
userFVPProfileDao = UserFVPProfileDao()