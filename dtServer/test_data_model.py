import sys
sys.path.append('./')
from peewee import *
from dtServer.data.conn import make_database_connection
from datetime import date

db = make_database_connection()

class TempDataModel(Model) : 

    data_type_1 = CharField(128)
    data_type_2 = CharField(128)
    created_date = DateField('%y-%m-%d')
    value = IntegerField()

    class Meta : 
        database = db
        table_name = 'temp_data'

def create_test_data() : 
    return [
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-01', 'value' : 10 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-01', 'value' : 10 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_B', 'created_date' : '2025-02-01', 'value' : 20 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_B', 'created_date' : '2025-02-01', 'value' : 20 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_B', 'created_date' : '2025-02-01', 'value' : 20 },

        {'data_type_1' : 'TYPE_1_B', 'data_type_2' : 'TYPE_2_C', 'created_date' : '2025-02-02', 'value' : 30 },
        {'data_type_1' : 'TYPE_1_B', 'data_type_2' : 'TYPE_2_C', 'created_date' : '2025-02-02', 'value' : 30 },
        {'data_type_1' : 'TYPE_1_B', 'data_type_2' : 'TYPE_2_C', 'created_date' : '2025-02-02', 'value' : 30 },
        {'data_type_1' : 'TYPE_1_B', 'data_type_2' : 'TYPE_2_D', 'created_date' : '2025-02-02', 'value' : 40 },
        {'data_type_1' : 'TYPE_1_B', 'data_type_2' : 'TYPE_2_D', 'created_date' : '2025-02-02', 'value' : 40 },

        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-03', 'value' : 50 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-03', 'value' : 50 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-03', 'value' : 50 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-03', 'value' : 50 },
        {'data_type_1' : 'TYPE_1_A', 'data_type_2' : 'TYPE_2_A', 'created_date' : '2025-02-03', 'value' : 50 },
    ]

def insert_test_data(list_data) : 

    with db.atomic() : 
        TempDataModel.insert_many(list_data).execute()

TempDataModel.drop_table(False)
TempDataModel.create_table(False)
insert_test_data( create_test_data() )