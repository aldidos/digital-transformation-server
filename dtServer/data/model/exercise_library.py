from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment
from dtServer.data.model.exercise_library_difficulty import ExerciseLibraryDifficulty
from dtServer.data.model.exercise_library_type import ExerciseLibraryType
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_MUSCLE_GROUP = 128

class ExerciseLibrary(BaseModel) : 
    name = CharField(LEN_NAME, index = True)
    type = ForeignKeyField(ExerciseLibraryType)
    equipment = ForeignKeyField(ExerciseLibraryEquipment)
    difficult = ForeignKeyField(ExerciseLibraryDifficulty)
    description = TextField(True)

    class Meta : 
        table_name = 'exercise_library'

def save_exercise_library(data : dict) : 
    model = dict_to_model(ExerciseLibrary, data)
    model.save()
    return model_to_dict(model)

def select_exericse_libraries() : 
    q = ExerciseLibrary.select()
    exercise_libs = [ model_to_dict(row) for row in q ]
    return exercise_libs

def select_exercise_library(name : str ) :
    model = ExerciseLibrary.get_or_none(ExerciseLibrary.name == name)
    return model_to_dict_or_none(model)
    
def insert_many_exercise_libraries(list_data) : 
    with db_proxy.atomic() : 
        ExerciseLibrary.insert_many(list_data).execute()



