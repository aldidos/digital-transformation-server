from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserExerciseMetric(BaseModel) : 
    user = ForeignKeyField(User)
    exercise_library = ForeignKeyField(ExerciseLibrary)
    num_sets = IntegerField()
    date = DateTimeField('%y-%m-%d %H:%M:%S')
    
    class Meta : 
        table_name = 'user_exercise_metric'

def save_user_exercise_metric(data : dict) : 
    model = dict_to_model(UserExerciseMetric, data)
    model.save()
    return model_to_dict(model)

def select_user_exer_metric(user : int, exercise_library : int) : 
    user_exercise_metric = UserExerciseMetric.get_or_none(UserExerciseMetric.user == user and UserExerciseMetric.exercise_library == exercise_library)
    return model_to_dict_or_none(user_exercise_metric)

def select_user_exer_metrics(user : int) : 
    q = UserExerciseMetric.select().where(UserExerciseMetric.user == user)
    list_data = [model_to_dict(row) for row in q]
    return list_data