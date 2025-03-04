import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.ormworkout.ormworkout_dao import ormWorkoutDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_insert() : 
    user_id = 1
    equipment_id = 11
    date = '2025-02-27'

    id = ormWorkoutDao.insert( user_id, equipment_id, date )
    print(id)

def test_get_most_recent_by_equipment() : 
    user_id = 1
    equipment_id = 11

    ormworkout = ormWorkoutDao.get_most_recent_by_equipment(user_id, equipment_id)
    print(ormworkout)

def test_get_recent_by_equipment() : 
    user_id = 1
    equipment_id = 11

    ormworkouts = ormWorkoutDao.get_recent_by_equipment(user_id, equipment_id)
    print(ormworkouts)

test_insert()
test_get_most_recent_by_equipment()
test_get_recent_by_equipment()