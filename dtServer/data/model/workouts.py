from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.center_equipment import CenterEquipment
from playhouse.shortcuts import model_to_dict, dict_to_model

class Workouts(BaseModel) : 
    workout_session_id = ForeignKeyField(WorkoutSessions)
    center_equipment_id = ForeignKeyField(CenterEquipment)
    completed_sets = IntegerField()
    start_time = TimestampField()
    end_time = TimestampField()

    class Meta : 
        table_name = 'workouts'

def save_workout(data : dict) : 
    model = dict_to_model(Workouts, data)
    n = model.save()
    if n > 0 : 
        return model, True
    return None, False

def select_workout_by_id(id : int) : 
    try : 
        workout = Workouts.get_by_id(id)
        return model_to_dict(workout)
    except DoesNotExist : 
        return None

def select_workout(id : int) : 
    workout = Workouts.select().where(Workouts.id == id).get()
    return model_to_dict(workout)

def select_workouts(workout_session_id : int) : 
    q = Workouts.select().where( Workouts.workout_session_id == workout_session_id )
    list_data = [model_to_dict(row) for row in q]
    return list_data