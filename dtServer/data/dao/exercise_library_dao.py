from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.exercise_library import ExerciseLibrary, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibraryDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(ExerciseLibrary, data) )
    
    def select_all(self) : 
        q = ExerciseLibrary.select()
        exercise_libs = [ model_to_dict(row) for row in q ]
        return exercise_libs

    def select_by_name(self, name : str ) :
        model = ExerciseLibrary.get_or_none(ExerciseLibrary.name == name)
        return model_to_dict_or_none(model)
        
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            ExerciseLibrary.insert_many(list_data).execute()

exerciseLibraryDao = ExerciseLibraryDao()