from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_MUSCLE_GROUP = 128

class ExerciseLibrary(BaseModel) : 
    name = CharField(LEN_NAME, index = True)
    type = IntegerField(False)
    equipment = ForeignKeyField(ExerciseLibraryEquipment)
    difficult = IntegerField()
    # muscle_group = CharField(LEN_MUSCLE_GROUP)

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
    return ExerciseLibrary.get_or_none(ExerciseLibrary.name == name)
    
def insert_many_exercise_libraries(list_data) : 
    with db_proxy.atomic() : 
        ExerciseLibrary.insert_many(list_data).execute()