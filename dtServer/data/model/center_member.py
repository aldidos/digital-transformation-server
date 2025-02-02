from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 20
DATE_FORMAT = '%y-%m-%d'
LEN_CONTACT = '16'

class CenterMember(BaseModel) : 
    center_id = ForeignKeyField(Center)
    name = CharField(LEN_NAME, index=True)
    birth_day = DateField(DATE_FORMAT)
    contact = CharField(LEN_CONTACT)
    reg_from = DateField(DATE_FORMAT)
    reg_to = DateField(DATE_FORMAT)
    visit_date = DateField(DATE_FORMAT, null = True)
    
    class Meta : 
        table_name = 'center_member'

def save_center_member(data : dict) : 
    model = dict_to_model(CenterMember, data)
    model.save()
    return model_to_dict(model)    

def select_center_members(center_id : int) : 
    q = CenterMember.select().where(CenterMember.center_id == center_id)
    center_members = [ model_to_dict( row ) for row in q ]
    return center_members

def select_center_member_by_id(center_member_id) : 
    center_member = CenterMember.get_or_none(CenterMember.id == center_member_id)
    return model_to_dict_or_none(center_member)

def get_center_member(center_id, name, birth_day, contact) : 
    center_member = CenterMember.get_or_none(CenterMember.center_id == center_id and CenterMember.name == name and CenterMember.birth_day == birth_day and CenterMember.contact == contact)
    return model_to_dict_or_none(center_member)

def insert_center_members(list_data) : 
    with db_proxy.atomic() : 
        CenterMember.insert_many(list_data).execute()