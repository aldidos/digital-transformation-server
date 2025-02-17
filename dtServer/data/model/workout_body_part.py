from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.body_part import BodyPart

class WorkoutBodypart(BaseModel) : 
    workout = ForeignKeyField(Workouts)   
    body_part = ForeignKeyField(BodyPart)

    class Meta  :
        table_name = 'workout_bodypart'