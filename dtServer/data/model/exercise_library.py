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


