from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class Workouts(BaseModel) : 
    workout_session = ForeignKeyField(WorkoutSessions)   
    exercise_library = ForeignKeyField(ExerciseLibrary)
    completed_sets = IntegerField()
    start_time = DateTimeField('%y-%m-%d %H:%M:%S')
    end_time = DateTimeField('%y-%m-%d %H:%M:%S')

    class Meta : 
        table_name = 'workouts'

def save_workout(data : dict) : 
    model = dict_to_model(Workouts, data)
    model.save()
    return model_to_dict(model)

def select_workout_by_id(id : int) : 
    workout =  Workouts.get_or_none(Workouts.id == id)    
    return model_to_dict_or_none(workout)

def select_workouts_by_workout_session_id(workout_session_id : int) : 
    q = Workouts.select().where( Workouts.workout_session == workout_session_id )
    list_data = [model_to_dict(row) for row in q]
    return list_data

def select_workouts(user_id, from_date, to_date) : 
    q = Workouts.select( ExerciseLibrary.name.alias('exercise_library_name'), Workouts.completed_sets, Workouts.start_time, Workouts.end_time)\
        .join(WorkoutSessions)\
        .join(User)\
        .join_from(Workouts, ExerciseLibrary)\
        .where(WorkoutSessions.is_completed == True, User.id == user_id,  WorkoutSessions.date.between(from_date, to_date))
    
    return [ row for row in q.dicts() ]
  
def insert_workouts(list_data) : 
    with db_proxy.atomic() :
        Workouts.insert_many(list_data).execute()