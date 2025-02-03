from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutMetrics(BaseModel) : 
    workout_sessions_id = ForeignKeyField(WorkoutSessions)
    user_id = ForeignKeyField(User)
    workout_id = ForeignKeyField(Workouts)
    timestamp = DateTimeField()
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

    class Meta : 
        table_name = 'workout_metrics'

def save_workout_metric(data) : 
    model = dict_to_model(WorkoutMetrics, data)
    model.save()
    return model_to_dict(model)

def insert_many_workout_metrics(list_data) : 
    with db_proxy.atomic() : 
        WorkoutMetrics.insert_many(list_data).execute()

def select_join_with_workout_sessions(user_id, from_date, to_date) : 
    q = WorkoutMetrics.select(WorkoutMetrics.add_index)\
        .join(WorkoutSessions)\
        .where(WorkoutSessions.user_id == user_id and WorkoutSessions.date.between(from_date, to_date) )
    list_data = [ model_to_dict( row ) for row in q ]
    return list_data