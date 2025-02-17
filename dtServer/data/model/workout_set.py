from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, TIME_FORMAT, DATETIME_FORMAT
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutSet(BaseModel) :
    workout = ForeignKeyField(Workouts)
    set = IntegerField(False)    
    weight = FloatField()
    total_reps = IntegerField(default = 0)
    set_start_time = DateTimeField(DATETIME_FORMAT, null = True)
    set_end_time = DateTimeField(DATETIME_FORMAT, null = True)
    res_start_time = DateTimeField(DATETIME_FORMAT, null = True)
    res_end_time = DateTimeField(DATETIME_FORMAT, null = True)
    
    class Meta : 
        table_name = 'wokrout_set'
