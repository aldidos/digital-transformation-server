import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout.workout_set_dao import workoutSetDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_get_by_id() : 
    id = 1    
    data = workoutSetDao.get_by_id(id)
    print(data)

def test_get_recent_by_exerciselibrary() : 
    user_id = 1
    exercise_library_id = 1
    set = 1

    workout_set = workoutSetDao.get_recent_by_exerciselibrary(user_id, exercise_library_id, set)
    print(workout_set)

def test_get_recent_by_equipment() : 
    user_id = 1
    equipment_id = 11
    set = 1

    workout_set = workoutSetDao.get_recent_by_equipment(user_id, equipment_id, set)
    print(workout_set)

def test_get_recent_by_bodypart() : 
    user_id = 1
    body_part_id = 4
    set = 1

    workout_set = workoutSetDao.get_recent_by_bodypart(user_id, body_part_id, set)
    print(workout_set)

test_get_by_id()
test_get_recent_by_exerciselibrary()
test_get_recent_by_equipment()
test_get_recent_by_bodypart()