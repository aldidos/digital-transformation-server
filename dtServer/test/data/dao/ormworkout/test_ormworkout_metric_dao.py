import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.ormworkout.ormworkout_metric_dao import ormWorkoutMetricDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_insert_many() : 
    dataset = [
        { 'ormworkout' : 1, 'weight' : 100, 'mean_velocity' : 0.75, 'mean_power' : 1024  },
        { 'ormworkout' : 1, 'weight' : 100, 'mean_velocity' : 0.75, 'mean_power' : 1024  },
        { 'ormworkout' : 1, 'weight' : 100, 'mean_velocity' : 0.75, 'mean_power' : 1024  } 
        ]    
    
    ormWorkoutMetricDao.insert_many(dataset)

def test_select_by_ormworkout_id() : 
    ormworkout_id = 1
    orm_metric = ormWorkoutMetricDao.select_by_ormworkout_id(ormworkout_id)
    print(orm_metric)

def test_select_recent_by_exerciselibrary() : 
    user_id = 1
    exercise_library_id = 12
    orm_metric = ormWorkoutMetricDao.select_recent_by_exerciselibrary(user_id, exercise_library_id)
    print(orm_metric)    

test_insert_many()
test_select_by_ormworkout_id()
test_select_recent_by_exerciselibrary()