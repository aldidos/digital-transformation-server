from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_TYPE_NAME = 512

class ExerciseLibraryType(BaseModel) : 
    type_name = CharField(LEN_TYPE_NAME, index = True) 

    class Meta : 
        table_name = 'exercise_library_type'

