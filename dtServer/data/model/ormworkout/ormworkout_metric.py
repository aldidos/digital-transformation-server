from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.ormworkout.ormworkout import ORMWorkout

class ORMWorkoutMetric(BaseModel) : 
    ormworkout = ForeignKeyField(ORMWorkout)
    weight = FloatField()
    mean_velocity = FloatField()
    mean_power = FloatField()
    
    class Meta : 
        table_name = 'ormworkout_metric'