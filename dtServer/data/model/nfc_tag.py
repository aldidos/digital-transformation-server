from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy, model_to_dict_or_none
from dtServer.data.model.center_equipment import CenterEquipment
from playhouse.shortcuts import model_to_dict, dict_to_model

LEN_NFC_TAG_ID = 32

class NFCTag(BaseModel) : 
    nfc_tag_id = CharField(LEN_NFC_TAG_ID, unique = True) 
    center_equipment = ForeignKeyField(CenterEquipment, index = True)
    
    class Meta : 
        table_name = 'nfc_tags'
