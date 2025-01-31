from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.center_equipment import CenterEquipment
from playhouse.shortcuts import model_to_dict, dict_to_model

class Workouts(BaseModel) : 
    workout_session_id = ForeignKeyField(WorkoutSessions)
    center_equipment_id = ForeignKeyField(CenterEquipment)
    completed_sets = IntegerField()
    start_time = TimeField('%H:%M:%S')
    end_time = TimeField('%H:%M:%S')

    class Meta : 
        table_name = 'workouts'

def save_workout(data : dict) : 
    model = dict_to_model(Workouts, data)
    model.save()
    return model_to_dict(model)

def select_workout_by_id(id : int) : 
    return Workouts.get_or_none(Workouts.id == id)    

def select_workouts(workout_session_id : int) : 
    q = Workouts.select().where( Workouts.workout_session_id == workout_session_id )
    list_data = [model_to_dict(row) for row in q]
    return list_data

def insert_workouts(list_data) : 
    with db_proxy.atomic() :
        Workouts.insert_many(list_data).execute()