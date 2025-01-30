from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserSurvey(BaseModel) : 
    user_id = ForeignKeyField(User)
    workout_goal = CharField(128)

    class Meta : 
        table_name = 'user_survey'

def save_user_survey(data : dict) :
    model = dict_to_model(UserSurvey, data)
    n = model.save()
    if n > 0 : 
        return True
    return False    

def select_user_survey(user_id : int) :
    try : 
        data = UserSurvey.select().where(UserSurvey.user_id == user_id).get()
        return model_to_dict(data)
    except DoesNotExist : 
        return None