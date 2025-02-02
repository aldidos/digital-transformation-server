from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_ADDRESS = 512

class Center(BaseModel) : 
    name = CharField(LEN_NAME, index = True)
    address = CharField(LEN_ADDRESS, index = True) 
    
    class Meta : 
        table_name = 'center'

def save_center(data : dict ) -> int :
    model = dict_to_model(Center, data)
    model.save()
    return model_to_dict(model)

def get_center_by_id(center_id : int) : 
    center =  Center.get_or_none(Center.id == center_id)
    return model_to_dict_or_none(center)

def get_center_by_name_address(center_name : str, address : str ) :
    center = Center.get_or_none(Center.center_name == center_name and Center.address == address) 
    return model_to_dict_or_none(center)

def insert_centers(list_data) : 
    with db_proxy.atomic() : 
        Center.insert_many(list_data).execute()