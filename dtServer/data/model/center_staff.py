from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center import Center
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
DATE_FORMAT = '%y-%m-%d'

class CenterStaff(BaseModel) : 
    center_id = ForeignKeyField(Center)    
    name = CharField(LEN_NAME, index=True)
    birth_day = DateField(DATE_FORMAT)

    class Meta : 
        table_name = 'center_staff'

def save_center_staff(data : dict) : 
    model = dict_to_model(CenterStaff, data) 
    model.save()
    return model_to_dict(model)      

def select_center_staffs(center_id : int) : 
    q = CenterStaff.select().where(CenterStaff.center_id == center_id)
    center_staffs = [model_to_dict(row) for row in q]    
    return center_staffs

def select_center_staff(id : int) : 
    center_staff = CenterStaff.get_or_none(CenterStaff.id == id)    
    return model_to_dict_or_none(center_staff)

def insert_center_staffs(list_data) : 
    with db_proxy.atomic() :
        CenterStaff.insert_many(list_data).execute()