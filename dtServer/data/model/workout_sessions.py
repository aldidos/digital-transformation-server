from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.user import User
from datetime import date
from playhouse.shortcuts import model_to_dict, dict_to_model

DATE_FORMAT = '%y-%m-%d'
LEN_STATUS = 20

class WorkoutSessions(BaseModel) : 
    user = ForeignKeyField(model = User)
    date = DateField(DATE_FORMAT, index=True)
    status = CharField(LEN_STATUS)
    is_completed = BooleanField(False)

    class Meta : 
        table_name = 'workout_sessions'

def create_workout_session(user_id, date, status) : 
    data = {
        'user' : user_id, 
        'date' : date, 
        'status' : status, 
        'is_completed' : False
    }
    return save_workout_session(date)

def save_workout_session(data : dict) : 
    model = dict_to_model(WorkoutSessions, data)
    model.save()
    return model_to_dict(model)

def select_workout_session(id) : 
    model = WorkoutSessions.select().where(WorkoutSessions.id == id).get()
    return model_to_dict(model)

def select_workout_sessions(user_id : int, date : date) : 
    q = WorkoutSessions.select().where( WorkoutSessions.user_id == user_id and WorkoutSessions.date == date )
    list_data = [model_to_dict(row) for row in q]
    return list_data

def select_workout_sessions_period(user_id : int, from_date : date, to_date : date) : 
    q = WorkoutSessions.select().where( WorkoutSessions.user_id == user_id and WorkoutSessions.date.between(from_date, to_date) )
    list_data = [model_to_dict(row) for row in q]
    return list_data

def insert_workout_sessions(list_data) : 
    with db_proxy.atomic() :
        WorkoutSessions.insert_many(list_data).execute()