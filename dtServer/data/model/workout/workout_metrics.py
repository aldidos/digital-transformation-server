from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, TIME_FORMAT
from dtServer.data.model.workout.workout_set import WorkoutSet
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutMetrics(BaseModel) :
    workout_set = ForeignKeyField(WorkoutSet)
    rep = IntegerField(False)
    mean_velocity = FloatField()
    peak_velocity = FloatField()
    mean_power = FloatField()
    peak_power = FloatField()
    mean_force = FloatField()
    peak_force = FloatField()
    peak_velocity_con = FloatField()
    mean_velocity_con = FloatField()
    peak_power_con = FloatField()
    mean_power_con = FloatField()
    peak_force_con = FloatField()
    mean_force_con = FloatField()
    peak_acceleration_con = FloatField()
    mean_acceleration_con = FloatField()
    peak_velocity_ecc = FloatField()
    mean_velocity_ecc = FloatField()
    peak_power_ecc = FloatField()
    mean_power_ecc = FloatField()
    peak_force_ecc = FloatField()
    mean_force_ecc = FloatField()
    peak_acceleration_ecc = FloatField()
    mean_acceleration_ecc = FloatField()    
    rep_duration_con = TimeField(TIME_FORMAT)
    rep_duration_ecc = TimeField(TIME_FORMAT)
    top_stay_duration = TimeField(TIME_FORMAT)
    bottom_stay_duration = TimeField(TIME_FORMAT)
    rep_duration = TimeField(TIME_FORMAT)
    RSI = FloatField()
    RFD = FloatField()
    
    class Meta : 
        table_name = 'workout_metrics'
