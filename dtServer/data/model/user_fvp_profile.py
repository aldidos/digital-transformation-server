from peewee import *
from dtServer.data.model.base_model import BaseModel, DATE_FORMAT
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary

class UserFVPProfile(BaseModel) : 
    user = ForeignKeyField(User)
    exercise_library = ForeignKeyField(ExerciseLibrary)
    date = DateField(DATE_FORMAT)

    class Meta : 
        table_name = 'user_fvp_profile'