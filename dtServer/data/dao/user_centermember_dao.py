from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_centermember import UserCenterMember, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenterMemberDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserCenterMember, data) )
    
    def insert(self, user_id, centermember_id) : 
        data = {
            "user" : user_id, 
            "centermember" : centermember_id
        }
        return self.save(data)

    def get_by_user(self, user_id) : 
        model = UserCenterMember.get_or_none( UserCenterMember.user == user_id )     
        return model_to_dict_or_none(model)

    def get_by_center_member(self, centermember_id) : 
        model = UserCenterMember.get_or_none( UserCenterMember.centermember == centermember_id ) 
        return model_to_dict_or_none(model)
    
userCenterMemberDao = UserCenterMemberDao()