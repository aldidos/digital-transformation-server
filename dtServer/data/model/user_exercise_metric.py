from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserExerciseMetric(BaseModel) : 
    user_id = ForeignKeyField(User)
    exercise_library_id = ForeignKeyField(ExerciseLibrary)
    weight = FloatField()

    class Meta : 
        table_name = 'user_exercise_metric'

def create_user_exercise_metric(user_id, exercise_library_id, weight) : 
    data = {
        "user_id" : user_id, 
        "exercise_library_id" : exercise_library_id, 
        "weight" : weight
    }
    return save_user_exercise_metric(data)

def save_user_exercise_metric(data : dict) : 
    model = dict_to_model(UserExerciseMetric, data)
    model.save()
    return model_to_dict(model)

def select_user_exer_metric(user_id : int, exercise_library_id : int) : 
    user_exercise_metric = UserExerciseMetric.get_or_none(UserExerciseMetric.user_id == user_id and UserExerciseMetric.exercise_library_id == exercise_library_id)    
    return model_to_dict_or_none(user_exercise_metric)

def select_user_exer_metrics(user_id : int) : 
    q = UserExerciseMetric.select().where(UserExerciseMetric.user_id == user_id)
    list_data = [model_to_dict(row) for row in q]
    return list_data