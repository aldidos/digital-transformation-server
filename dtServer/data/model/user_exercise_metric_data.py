from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none, db_proxy
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user_exercise_metric import UserExerciseMetric
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserExerciseMetricData(BaseModel) : 
    user_exercise_metric_id = ForeignKeyField(UserExerciseMetric)
    weight = FloatField()
    set = IntegerField()
    rep = IntegerField()    
    peak_velocity_con = FloatField()
    mean_velocity_con = FloatField()    
    peak_power_con = FloatField()    
    mean_power_con = FloatField()
    weight_distance = FloatField()
    dip = FloatField()
    peak_velocity_ecc = FloatField()
    mean_velocity_ecc = FloatField()
    peak_power_ecc = FloatField()
    mean_power_ecc = FloatField()
    concentric_rep_duration = TimeField()
    rep_duration = TimeField()
    eccentric_rep_duration = TimeField()
    top_stay_duration = TimeField()
    bottom_stay_duration = TimeField()
    rep_start = TimeField()
    rep_end = TimeField()
    concentric_work = FloatField()
    concentric_work_power = FloatField()
    ecc_con_ration = FloatField()

    class Meta : 
        table_name = 'user_exercise_metric_data'

def save_user_exercise_metric_data(data : dict) : 
    model = dict_to_model(UserExerciseMetricData, data)
    model.save()
    return model_to_dict(model)

def insert_many_exercise_metric_data(list_data ) : 
    with db_proxy.atomic() :
        UserExerciseMetricData.insert_many(list_data).execute()

def select_exercise_metric_datas(user_exercise_metric_id : int) : 
    q = UserExerciseMetricData.select().where(UserExerciseMetricData.user_exercise_metric_id == user_exercise_metric_id)
    list_data = [model_to_dict(row) for row in q]
    return list_data