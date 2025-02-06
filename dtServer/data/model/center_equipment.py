from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center import Center
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterEquipment (BaseModel) : 
    center = ForeignKeyField(Center)
    equipment = ForeignKeyField(ExerciseLibraryEquipment)
    exercise_library = ForeignKeyField(ExerciseLibrary) 
    location_x = FloatField(False)
    location_y = FloatField(False)
    usage = BooleanField(default=False)
    
    class Meta : 
        table_name = 'center_equipment'

