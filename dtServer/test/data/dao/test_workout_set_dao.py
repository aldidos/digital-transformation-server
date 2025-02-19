import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout_set_dao import workoutSetDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_get_by_id() : 
    id = 1
    
    data = workoutSetDao.get_by_id(id)

    print(data)

test_get_by_id()