from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.user import User
from dtServer.data.model.exercise_library import ExerciseLibrary

class UserFVPProfile(BaseModel) : 
    user = ForeignKeyField(User)
    exercise_library = ForeignKeyField(ExerciseLibrary)
    # Force = FloatField()
    # Velocity = FloatField()
    # Power = FloatField()
    # minimal_velocity_threshold = FloatField()

    class Meta : 
        table_name = 'user_fvp_profile'