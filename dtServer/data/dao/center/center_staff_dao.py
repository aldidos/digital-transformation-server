from dtServer.data.dao.base_dao import BaseDAO 
from dtServer.data.model.base_model import db_proxy, model_to_dict_or_none
from dtServer.data.model.center.center_staff import CenterStaff
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterStaffDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(CenterStaff, data) )
    
    def select_by_center_id(self, center_id : int) : 
        q = CenterStaff.select().where(CenterStaff.center == center_id)
        center_staffs = [model_to_dict(row) for row in q]    
        return center_staffs

    def get_by_id(self, id : int) : 
        center_staff = CenterStaff.get_or_none(CenterStaff.id == id)    
        return model_to_dict_or_none(center_staff)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            return CenterStaff.insert_many(list_data).execute()

centerStaffDao = CenterStaffDao()