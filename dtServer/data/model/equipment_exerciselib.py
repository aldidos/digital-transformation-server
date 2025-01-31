from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class EquipmentExerciseLib(BaseModel) : ####
    equipment_id = ForeignKeyField(ExerciseLibraryEquipment)
    exercise_library_id = ForeignKeyField(ExerciseLibrary)

    class Meta : 
        table_name = 'equipment_exerciselib'

def save_equipment_exercise_lib(data : dict) : 
    model = dict_to_model(EquipmentExerciseLib, data)
    model.save()
    return model_to_dict(model)

def get_equipment_exercise_lib_by_equipment_id(equipment_id : int) :
    data_model = EquipmentExerciseLib.select().where( EquipmentExerciseLib.equipment_id == equipment_id ).get()
    return model_to_dict(data_model)

def get_equipment_exercise_lib_by_exercise_library_id(exercise_library_id : int) :
    data_model = EquipmentExerciseLib.select().where( EquipmentExerciseLib.exercise_library_id == exercise_library_id ).get()
    return model_to_dict(data_model)