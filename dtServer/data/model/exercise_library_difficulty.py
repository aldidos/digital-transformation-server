from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_DIFFICULTY = 512

class ExerciseLibraryDifficulty(BaseModel) : 
    difficulty = CharField(LEN_DIFFICULTY, index = True) 

    class Meta : 
        table_name = 'exercise_library_difficulty'

