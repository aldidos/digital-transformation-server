from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserSurvey(BaseModel) : 
    user = ForeignKeyField(User)
    workout_goal = IntegerField(null = False)
    workout_level = IntegerField(null = False)

    class Meta : 
        table_name = 'user_survey'