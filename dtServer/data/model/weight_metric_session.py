from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class WeightMetricSession(BaseModel) : 
    user = ForeignKeyField(User)
    exercise_library = ForeignKeyField(ExerciseLibrary)
    num_sets = IntegerField()
    date = DateTimeField('%y-%m-%d %H:%M:%S')
    
    class Meta : 
        table_name = 'user_exercise_metric_session'

