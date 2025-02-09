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
    peak_velocity_con = FloatField()
    mean_velocity_con = FloatField()
    peak_power_con = FloatField()
    mean_power_con = FloatField()
    peak_foce_con = FloatField()
    mean_foce_con = FloatField()
    peak_acceleration_con = FloatField()
    mean_acceleration_con = FloatField()
    peak_velocity_ecc = FloatField()
    mean_velocity_ecc = FloatField()
    peak_power_ecc = FloatField()
    mean_power_ecc = FloatField()
    peak_foce_ecc = FloatField()
    mean_foce_ecc = FloatField()
    peak_acceleration_ecc = FloatField()
    mean_acceleration_ecc = FloatField()    
    # rep_duration_con = TimeField('%H:%M:%S')
    # rep_duration_ecc = TimeField('%H:%M:%S')
    # top_stay_duration = TimeField('%H:%M:%S')    
    # bottom_stay_duration = TimeField('%H:%M:%S')    
    # rep_start = DateTimeField('%y-%m-%d %H:%M:%S')
    # rep_end = DateTimeField('%y-%m-%d %H:%M:%S')
    rep_duration_con = FloatField()
    rep_duration_ecc = FloatField()
    top_stay_duration = FloatField()
    bottom_stay_duration = FloatField()
    rep_duration = FloatField()
    RSI = FloatField()
    RFD = FloatField()
    
    class Meta : 
        table_name = 'workout_metrics'
