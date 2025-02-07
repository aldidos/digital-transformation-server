from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment
from dtServer.data.model.exercise_library import ExerciseLibrary

class EquipmentExerciseLib(BaseModel) : ####
    equipment = ForeignKeyField(ExerciseLibraryEquipment)
    exercise_library = ForeignKeyField(ExerciseLibrary)

    class Meta : 
        table_name = 'equipment_exerciselib'
