import sys
sys.path.append("./")

from peewee import *
from dtServer.data.conn import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.data.data_converter import *

class TestDataModel(Model) : 
    name = CharField(512)
    b = BooleanField()
    temp = IntegerField()
    date = DateField('%y-%m-%d')

    class Meta : 
        database = db_proxy
        table_name = 'test_data'

tables = [TestDataModel]

conn = make_database_connection()
db_proxy.initialize(conn)

# conn.drop_tables(tables, safe = True)
# conn.create_tables(tables)

data = {        
    'name' : True, 
    'b' : 1204, 
    'date' : '2025-01-31'
}

model = dict_to_model(TestDataModel, data)
print(model.id)
model.save()
print(model.id)

print(type(model.date))

data = model_to_dict(model)
print(data)

data_a = TestDataModel.get_or_none(TestDataModel.id == 1)
print(data_a.name)