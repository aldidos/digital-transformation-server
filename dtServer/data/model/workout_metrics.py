from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutMetrics(BaseModel) :
    workout = ForeignKeyField(Workouts)
    set = IntegerField(False)
    rep = IntegerField(False)
    weight = FloatField()
    volume = FloatField()
    peak_velocity = FloatField()
    mean_velocity = FloatField()
    peak_power = FloatField()
    mean_power = FloatField()
    height = FloatField()
    power = FloatField(False)
    created_at = DateTimeField()

    class Meta : 
        table_name = 'workout_metrics'

def save_workout_metric(data) : 
    model = dict_to_model(WorkoutMetrics, data)
    model.save()
    return model_to_dict(model)

def insert_many_workout_metrics(list_data) : 
    with db_proxy.atomic() : 
        WorkoutMetrics.insert_many(list_data).execute()

def select_period_workout_metrics(user_id, from_date, to_date) : 
    q = WorkoutMetrics.select(Workouts.workout_session.date.alias('date'), ExerciseLibrary.name.alias('exercise_library_name'), WorkoutMetrics.set, WorkoutMetrics.rep\
                    , WorkoutMetrics.weight, WorkoutMetrics.volume, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.height, WorkoutMetrics.power )\
        .join(Workouts)\
        .join(WorkoutSessions)\
        .join(User)\
        .join_from(Workouts, ExerciseLibrary)\
        .where(User.id == user_id, WorkoutSessions.date.between(from_date, to_date) )
    
    list_data = [ row for row in q.dicts() ]
    return list_data
