from dtServer.data.model.base_model import db_proxy
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
            "center_member" : centermember_id
        }
        return self.save(data)

    def get_by_user(self, user_id) : 
        q = UserCenterMember.select().where( UserCenterMember.user == user_id )
        return [ row for row in q.dicts() ]

    def get_by_center_member(self, centermember_id) : 
        q = UserCenterMember.select().where( UserCenterMember.center_member == centermember_id )
        return [ row for row in q.dicts() ]
    
    def get_by_user_and_center(self, user_id, center_id) : 
        model = UserCenterMember.get_or_none( UserCenterMember.user == user_id, UserCenterMember.center == center_id )
        return model_to_dict_or_none(model)
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            UserCenterMember.insert_many(list_data).execute()
    
userCenterMemberDao = UserCenterMemberDao()