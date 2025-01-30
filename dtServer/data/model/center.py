from peewee import *
from dtServer.data.model.base_model import BaseModel
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NAME = 128
LEN_ADDRESS = 512

class Center(BaseModel) : 
    name = CharField(LEN_NAME, index=True)
    address = CharField(LEN_ADDRESS) 
    
    class Meta : 
        table_name = 'center'

def save_center(data : dict ) -> int :
    model = dict_to_model(Center, data)
    n = model.save()
    if n > 0 : 
        return True
    return False    

def get_center_by_id(center_id : int) : 
    try : 
        center = Center.get_by_id(center_id)
        return model_to_dict(center)
    except DoesNotExist : 
        return None

def select_center_by_id(center_id : int) : 
    try : 
        center = Center.get_by_id(center_id)
        return center        
    except DoesNotExist : 
        return None

def select_center_by_name_address(center_name : str, address : str ) :
    try : 
        center = Center.select().where( Center.center_name == center_name and Center.address == address ).get()
        return model_to_dict(center)
    except DoesNotExist : 
        return None

