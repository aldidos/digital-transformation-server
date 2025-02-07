from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibraryEquipmentDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(ExerciseLibraryEquipment, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            ExerciseLibraryEquipment.insert_many(list_data).execute()

exerciseLibraryEquipmentDao = ExerciseLibraryEquipmentDao()