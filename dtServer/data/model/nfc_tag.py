from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center_equipment import CenterEquipment
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NFC_TAG_ID = 32

class NFCTag(BaseModel) : 
    nfc_tag_id = CharField(LEN_NFC_TAG_ID, unique = True) 
    center_equipment_id = ForeignKeyField(CenterEquipment, index = True)
    
    class Meta : 
        table_name = 'nfc_tags'

def create_nfc_access(nfc_tag_id, center_equipment_id) : 
    data = {
        'nfc_tag_id' : nfc_tag_id, 
        'center_equipment_id' : center_equipment_id
    }
    return save_nfc_tag(data)

def save_nfc_tag(data) : 
    model = dict_to_model(NFCTag, data)
    model.save()
    return model_to_dict(model)

def select_nfc_tag(nfc_tag_id) : 
    nfc_tag = NFCTag.get_or_none( NFCTag.nfc_tag_id == nfc_tag_id )
    return model_to_dict_or_none(nfc_tag)

def insert_nfc_tags(list_data) : 
    with db_proxy.atomic() :
        NFCTag.insert_many(list_data).execute()