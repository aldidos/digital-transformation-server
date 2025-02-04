from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy

LEN_EQUIPMENT_TYPE = 512
LEN_NAME = 512

class ExerciseLibraryEquipment(BaseModel) : 
    id = PrimaryKeyField()
    equipment_type = CharField(LEN_EQUIPMENT_TYPE) ## weight, cadio, other
    is_machine = BooleanField(False) ## True : machine equipment, False : otherwise
    name = CharField(LEN_NAME)

    class Meta : 
        table_name = 'exerciselibrary_equipment'

def insert_exerciselibrary_equipments(list_data) : 
    with db_proxy.atomic() : 
        ExerciseLibraryEquipment.insert_many(list_data).execute()