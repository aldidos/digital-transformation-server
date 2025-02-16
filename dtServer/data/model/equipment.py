from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy

LEN_EQUIPMENT_TYPE = 512
LEN_NAME = 512

class Equipment(BaseModel) : 
    equipment_type = CharField(LEN_EQUIPMENT_TYPE) ## weight, cadio, other
    is_machine = BooleanField(False) ## True : machine equipment, False : otherwise
    name = CharField(LEN_NAME)

    class Meta : 
        table_name = 'equipment'

