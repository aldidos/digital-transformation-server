from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.center_member import CenterMember, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterMemberDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(CenterMember, data) )
    
    def select_by_center_id(self, center_id : int) : 
        q = CenterMember.select().where(CenterMember.center == center_id)
        center_members = [ model_to_dict( row ) for row in q ]
        return center_members

    def select_by_center_member_id(self, center_member_id) : 
        center_member = CenterMember.get_or_none(CenterMember.id == center_member_id)
        return model_to_dict_or_none(center_member)

    def get(self, center_id, name, birth_day, contact) : 
        center_member = CenterMember.get_or_none(CenterMember.center == center_id and CenterMember.name == name and CenterMember.birth_day == birth_day and CenterMember.contact == contact)
        return model_to_dict_or_none(center_member)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            CenterMember.insert_many(list_data).execute()

centerMemberDao = CenterMemberDao()