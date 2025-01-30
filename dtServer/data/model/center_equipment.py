from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.center import Center
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class CenterEquipment (BaseModel) : 
    center_id = ForeignKeyField(Center)
    equipment_id = ForeignKeyField(Equipment)
    exercise_library_id = ForeignKeyField(ExerciseLibrary) 
    location_x = FloatField(False)
    location_y = FloatField(False)
    usage = BooleanField(default=False)
    
    class Meta : 
        table_name = 'center_equipment'

def save_center_euipment( data : dict) : 
    center_euipment = dict_to_model(CenterEquipment, data)    
    n = center_euipment.save()    
    if n > 0 : 
        return True
    return False

def select_center_euipments( center_id : int) : 
    query = CenterEquipment.select().where(CenterEquipment.center_id == center_id )
    center_equipments = [ model_to_dict(CenterEquipment, row) for row in query ]
    return center_equipments

def select_center_euipment( id : int ) : 
    center_equipment = CenterEquipment.select().where(CenterEquipment.id == id ).get()
    return model_to_dict(center_equipment)

