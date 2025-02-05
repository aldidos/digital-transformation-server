from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.user import User
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.exerciselib_bodypart import select_bodyparts
from dtServer.data.model.body_part import BodyPart
from dtServer.data.model.workout_metrics import WorkoutMetrics, save_workout_metric
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutData(BaseModel) :
    workout_session = ForeignKeyField(WorkoutSessions) 
    workout = ForeignKeyField(Workouts) 
    exercise_library = ForeignKeyField(ExerciseLibrary) 
    body_part = ForeignKeyField(BodyPart) 
    workout_metric = ForeignKeyField(WorkoutMetrics) 
    
    class Meta : 
        table_name = 'workout_data'

def insert_many_workout_data(workout_session_id, workout_id, workout_metrics) : 
    with db_proxy.atomic() : 
        workout = Workouts.get_by_id(workout_id)
        
        list_workout_metrics = []
        for workout_metric in workout_metrics : 
                saved_workout_metric = save_workout_metric(workout_metric)
                list_workout_metrics.append(saved_workout_metric)

        body_parts = select_bodyparts(workout.exercise_library.id)

        list_workout_data = []
        for body_part in body_parts : 
            for workout_metric in list_workout_metrics : 
                list_workout_data.append({
                    'workout_session' : workout_session_id, 
                    'workout' : workout.id,
                    'exercise_library' : workout.exercise_library.id,
                    'body_part' : body_part['id'],
                    'workout_metric' : workout_metric['id']
                })        
        WorkoutData.insert_many(list_workout_data).execute()

def select_workout_data_with_exercise_library(user_id, from_date, to_date) : 
    q = WorkoutData.select(WorkoutSessions.date, ExerciseLibrary.name, WorkoutMetrics.set, fn.AVG(WorkoutMetrics.peak_power).alias('avg_peak_power'))\
    .join(WorkoutSessions)\
    .join(User)\
    .switch(WorkoutData)\
    .join(ExerciseLibrary)\
    .switch(WorkoutData)\
    .join(WorkoutMetrics)\
    .where( WorkoutSessions.user.id == user_id, WorkoutSessions.date.between(from_date, to_date) )\
    .group_by(WorkoutSessions.date, ExerciseLibrary.name, WorkoutMetrics.set)
        
    return [ row for row in q.dicts() ]

def select_workout_data_with_body_parts(user_id, from_date, to_date) : 
    q = WorkoutData.select(WorkoutSessions.date, BodyPart.name, WorkoutMetrics.set, fn.AVG(WorkoutMetrics.peak_power).alias('avg_peak_power'))\
    .join(WorkoutSessions)\
    .join(User)\
    .switch(WorkoutData)\
    .join(BodyPart)\
    .switch(WorkoutData)\
    .join(WorkoutMetrics)\
    .where( WorkoutSessions.user.id == user_id, WorkoutSessions.date.between(from_date, to_date) )\
    .group_by(WorkoutSessions.date, BodyPart.name, WorkoutMetrics.set)

    return [ row for row in q.dicts() ]

def get_user_recent_workout_summary(user_id, from_date, to_date) : 
    q = WorkoutData.select().join()\
    .join(WorkoutSessions)\
    .join(User)\
    .switch(WorkoutData)\
    .join(WorkoutMetrics)\
    .where( WorkoutSessions.user.id == user_id, WorkoutSessions.date.between(from_date, to_date) )\
    .distict(True)    