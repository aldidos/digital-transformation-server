from peewee import *
from dtServer.data.model.base_model import BaseModel, DATE_FORMAT
from dtServer.data.model.user.user import User
from dtServer.data.model.equipment import Equipment

class ORMWorkout(BaseModel) : 
    user = ForeignKeyField(User)
    equipment = ForeignKeyField(Equipment)
    date = DateField(DATE_FORMAT, index = True)

    class Meta : 
        table_name = 'ormworkout'