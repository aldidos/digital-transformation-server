from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 20
DATE_FORMAT = '%y-%m-%d'
LEN_CONTACT = '16'

class CenterMember(BaseModel) : 
    center = ForeignKeyField(Center)
    name = CharField(LEN_NAME, index=True)
    birth_day = DateField(DATE_FORMAT, index=True)
    contact = CharField(LEN_CONTACT, index=True)
    reg_from = DateField(DATE_FORMAT)
    reg_to = DateField(DATE_FORMAT)
    visit_date = DateField(DATE_FORMAT, null = True)
    
    class Meta : 
        table_name = 'center_member'        

