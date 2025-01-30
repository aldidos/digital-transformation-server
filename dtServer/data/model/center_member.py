from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.util.json_encoder import encode

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
    visit_date = DateField(DATE_FORMAT)
    
    class Meta : 
        table_name = 'center_member'

def save_center_member(data : dict) : 
    model = dict_to_model(CenterMember, data)
    n = model.save()
    if n > 0 :
        return True
    return False    

def select_center_members(center_id : int) : 
    q = CenterMember.select().where(CenterMember.center_id == center_id)
    center_members = [ model_to_dict( row ) for row in q ]
    return center_members

def select_center_member_by_id(center_member_id) : 
    try : 
        center_member = CenterMember.get_by_id(center_member_id)
        return center_member
    except DoesNotExist : 
        return None

def select_center_member(center_id, name, birth_day, contact) : 
    try : 
        center_member = CenterMember.select().where(CenterMember.center_id == center_id and CenterMember.name == name and CenterMember.birth_day == birth_day and CenterMember.contact == contact).get()
        return model_to_dict(center_member)
    except DoesNotExist : 
        return None