from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.body_part import BodyPart
from dtServer.data.model.ormworkout.ormworkout import ORMWorkout

class ORMWorkoutBodypart(BaseModel) : 
    ormworkout = ForeignKeyField(ORMWorkout)
    body_part = ForeignKeyField(BodyPart)

    class Meta : 
        table_name = 'ormworkout_bodypart'