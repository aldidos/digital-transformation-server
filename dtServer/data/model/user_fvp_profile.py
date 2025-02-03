from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserFVPProfile(BaseModel) : 
    user_id = ForeignKeyField(User)
    exercise_library_id = ForeignKeyField(ExerciseLibrary)
    Force = FloatField()
    Velocity = FloatField()
    Power = FloatField()
    minimal_velocity_threshold = FloatField()

    class Meta : 
        table_name = 'user_fvp_profile'

def save_workout(data : dict) : 
    model = dict_to_model(UserFVPProfile, data)
    model.save()
    return model_to_dict(model)

def select_user_fvp_profiles(user_id) : 
    q = UserFVPProfile.select().where(UserFVPProfile.user_id == user_id)
    list_data = [ model_to_dict(row) for row in q ]
    return list_data

def select_user_fvp_profile(user_id, exercise_library_id) : 
    model = UserFVPProfile.get_or_none(UserFVPProfile.user_id == user_id and UserFVPProfile.exercise_library_id == exercise_library_id  )
    return model_to_dict_or_none(model)
    
