from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_centermember import UserCenterMember, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserCenterMemberDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserCenterMember, data) )
    
    def insert(self, user_id, center_id, centermember_id) : 
        data = {
            "user" : user_id, 
            'center' : center_id,
            "centermember" : centermember_id
        }
        return self.save(data)

    def get_by_user(self, user_id) : 
        q = UserCenterMember.select().where( UserCenterMember.user == user_id )
        return [ row for row in q.dicts() ]

    def get_by_center_member(self, centermember_id) : 
        q = UserCenterMember.select().where( UserCenterMember.centermember == centermember_id )
        return [ row for row in q.dicts() ]
    
    def get_by_user_and_center(self, user_id, center_id) : 
        model = UserCenterMember.get_or_none( UserCenterMember.user == user_id, UserCenterMember.center == center_id )
        return model_to_dict_or_none(model)
    
userCenterMemberDao = UserCenterMemberDao()