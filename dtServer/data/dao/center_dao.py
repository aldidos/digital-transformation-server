from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.center import Center, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(Center, data) )
    
    def get_by_id(self, id : int) : 
        center =  Center.get_or_none(Center.id == id)
        return model_to_dict_or_none(center)

    def get_by_name_and_address(self, center_name : str, address : str ) :
        center = Center.get_or_none(Center.name == center_name, Center.address == address) 
        return model_to_dict_or_none(center)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            Center.insert_many(list_data).execute()

centerDao = CenterDao()