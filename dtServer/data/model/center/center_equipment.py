from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center.center import Center
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterEquipment (BaseModel) : 
    center = ForeignKeyField(Center)
    equipment = ForeignKeyField(Equipment)
    location = IntegerField(null=False)
    usage = BooleanField(default=False)
    
    class Meta : 
        table_name = 'center_equipment'

