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

