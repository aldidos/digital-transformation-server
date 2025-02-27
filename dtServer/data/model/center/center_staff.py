from peewee import *
from dtServer.data.model.base_model import BaseModel, DATE_FORMAT
from dtServer.data.model.center.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128

class CenterStaff(BaseModel) : 
    center = ForeignKeyField(Center)    
    name = CharField(LEN_NAME, index=True)
    birth_day = DateField(DATE_FORMAT)

    class Meta : 
        table_name = 'center_staff'

