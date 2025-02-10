from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none, DATETIME_FORMAT
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class Workouts(BaseModel) : 
    workout_session = ForeignKeyField(WorkoutSessions)   
    exercise_library = ForeignKeyField(ExerciseLibrary)
    completed_sets = IntegerField()
    start_time = DateTimeField(DATETIME_FORMAT)
    end_time = DateTimeField(DATETIME_FORMAT)

    class Meta : 
        table_name = 'workouts'