from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.equipment import Equipment, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class EquipmentDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(Equipment, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            Equipment.insert_many(list_data).execute()

equipmentDao = EquipmentDao()