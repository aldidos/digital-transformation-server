from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.exercise_library_difficulty import ExerciseLibraryDifficulty, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibraryDifficultyDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(ExerciseLibraryDifficulty, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            ExerciseLibraryDifficulty.insert_many(list_data).execute()

exerciseLibraryDifficultyDao = ExerciseLibraryDifficultyDao()