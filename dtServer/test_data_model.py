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


from dtServer.data.model.base_model import db_proxy
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart, ExerciseLibrary, BodyPart
from dtServer.data.data_converter import model_to_dict_or_none
import json

db_proxy.initialize(db)

# q = ExerciseLibBodyPart.select(ExerciseLibBodyPart.exercise_library_id, ExerciseLibBodyPart.body_part_id  )\
q = ExerciseLibBodyPart.select(ExerciseLibBodyPart.body_part_id)\
                        .join(ExerciseLibrary, JOIN.INNER)\
                        .switch(ExerciseLibBodyPart)\
                        .join(BodyPart, JOIN.INNER)\
                        .where(ExerciseLibrary.id == 1)

# q = ExerciseLibrary.select(ExerciseLibrary.name, fn.COUNT(ExerciseLibBodyPart.body_part_id).alias('cnt')  )\
#                         .join(ExerciseLibBodyPart, JOIN.INNER)\
#                         .group_by(ExerciseLibrary.name) 

# q = ExerciseLibrary.select(ExerciseLibrary)

for row in q : 
    
    d = model_to_dict_or_none(row)
    print( json.dumps(d) )
    # print(row.exercise_library_id.id, row.body_part_id.id)
