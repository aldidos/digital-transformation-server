from peewee import *
from dtServer.data.model.base_model import BaseModel
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 100
LEN_TYPE = 50

class Equipment(BaseModel) : ####
    name = CharField(LEN_NAME, index = True)
    type = CharField(LEN_TYPE, index = True)
    specs = TextField()

    class Meta : 
        table_name = 'equipment'

def save_equipment(data : dict) : 
    model = dict_to_model(Equipment, data)
    model.save()
    return model_to_dict(model)

def select_equipments() : 
    q = Equipment.select()
    equipments = [model_to_dict(row) for row in q]
    return equipments