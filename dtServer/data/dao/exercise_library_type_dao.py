from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.exercise_library_type import ExerciseLibraryType, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibraryTypeDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(ExerciseLibraryType, data) )
    
    def insert_many_exercise_library_type(self, list_data) : 
        with db_proxy.atomic() : 
            ExerciseLibraryType.insert_many(list_data).execute()

exerciseLibraryTypeDao = ExerciseLibraryTypeDao()