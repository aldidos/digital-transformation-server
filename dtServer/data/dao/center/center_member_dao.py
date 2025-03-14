from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.center.center_member import CenterMember, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterMemberDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(CenterMember, data) )
    
    def select_by_center_id(self, center_id : int) : 
        q = CenterMember.select().where(CenterMember.center == center_id)
        center_members = [ model_to_dict( row ) for row in q ]
        return center_members
    
    def get_by_id(self, id) : 
        return model_to_dict_or_none( CenterMember.get_or_none( CenterMember.id == id ) )

    def get(self, center_id, name, birth_day, contact) : 
        center_member = CenterMember.get_or_none(CenterMember.center == center_id, CenterMember.name == name, CenterMember.birth_day == birth_day, CenterMember.contact == contact)
        return model_to_dict_or_none(center_member)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            CenterMember.insert_many(list_data).execute()

centerMemberDao = CenterMemberDao()