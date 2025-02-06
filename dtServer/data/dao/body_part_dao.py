from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.body_part import BodyPart, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class BodyPartDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(BodyPart, data) )
    
    def select_all(self) : 
        query = BodyPart.select()
        body_parts = [ model_to_dict(row) for row in query ]
        return body_parts

    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            BodyPart.insert_many(list_data).execute()


bodyPartDao = BodyPartDao()