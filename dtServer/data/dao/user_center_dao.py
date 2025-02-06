from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_center import UserCenter, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenterDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserCenter, data) )
    
    def create_user_center(self, user_id, center_id) : 
        data = {
            'user' : user_id, 
            'center' : center_id
        }
        return self.save(data)    

    def get_by_user(self, user_id : int) : 
        q = UserCenter.select().where(UserCenter.user == user_id)
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def get_by_user_and_center(self, user_id : int, center_id : int) : 
        model =  UserCenter.get_or_none(UserCenter.user == user_id and UserCenter.center == center_id)
        return model_to_dict_or_none(model)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            UserCenter.insert_many(list_data).execute()

userCenterDao = UserCenterDao()