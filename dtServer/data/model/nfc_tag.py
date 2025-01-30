from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from dtServer.data.model.center import Center
from dtServer.data.model.center_equipment import CenterEquipment
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NFC_TAG_ID = 32
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

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
    model = NFCTag.select().where( NFCTag.nfc_tag_id == nfc_tag_id ).get()
    return model_to_dict(model)