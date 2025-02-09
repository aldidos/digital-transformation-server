from dtServer.data.model.base_model import BaseModel, db_proxy 
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_CATEGORY = 512
LEN_SUB_CATEGORY = 512
LEN_MUSCLE_GROUP = 512

class BodyPart(BaseModel) :     
    category = CharField(LEN_CATEGORY) 
    sub_category = CharField(LEN_SUB_CATEGORY) 
    name = CharField(LEN_NAME)
    muscle_group = CharField(LEN_MUSCLE_GROUP)

    class Meta : 
        table_name = 'body_part'

