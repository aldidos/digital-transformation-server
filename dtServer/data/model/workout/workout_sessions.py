from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, DATE_FORMAT
from dtServer.data.model.user.user import User
from datetime import date
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_STATUS = 20

class WorkoutSessions(BaseModel) : 
    user = ForeignKeyField(model = User)
    date = DateField(DATE_FORMAT, index=True)
    status = CharField(LEN_STATUS)
    is_completed = BooleanField(False)

    class Meta : 
        table_name = 'workout_sessions'