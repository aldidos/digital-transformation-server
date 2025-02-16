from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.exercise_library import ExerciseLibrary

class EquipmentExerciseLib(BaseModel) : ####
    equipment = ForeignKeyField(Equipment)
    exercise_library = ForeignKeyField(ExerciseLibrary)

    class Meta : 
        table_name = 'equipment_exerciselib'
