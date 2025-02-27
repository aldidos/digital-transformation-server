from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.center.center_equipment import CenterEquipment, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterEquipmentDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(CenterEquipment, data) )
    
    def select_by_center_id(self,  center_id : int) : 
        query = CenterEquipment.select().where(CenterEquipment.center == center_id )
        center_equipments = [ model_to_dict(row) for row in query ]
        return center_equipments

    def get_by_id(self,  id : int ) : 
        center_equipment = CenterEquipment.get_or_none(CenterEquipment.id == id) 
        return model_to_dict_or_none(center_equipment)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            CenterEquipment.insert_many(list_data).execute()

centerEquipmentDao = CenterEquipmentDao()