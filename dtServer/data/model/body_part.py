from dtServer.data.model.base_model import BaseModel, db_proxy
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_CATEGORY = 512
LEN_SUB_CATEGORY = 512
LEN_MUSCLE_GROUP = 512

class BodyPart(BaseModel) :     
    category = CharField(LEN_CATEGORY) # upper body, lower body, whole body
    sub_category = CharField(LEN_SUB_CATEGORY) # Chest, Back, Shoulders, Arm, Abdominals, Hip, Legs, whole body
    name = CharField(LEN_NAME)
    muscle_group = CharField(LEN_MUSCLE_GROUP)

    class Meta : 
        table_name = 'body_part'

def save_body_part(data : dict) : 
    model = dict_to_model(BodyPart, data)    
    model.save()
    return model_to_dict(model)

def get_body_parts() : 
    query = BodyPart.select()
    body_parts = [ model_to_dict(row) for row in query ]
    return body_parts

def insert_body_parts(list_data) : 
    
    with db_proxy.atomic() : 
        BodyPart.insert_many(list_data).execute()   