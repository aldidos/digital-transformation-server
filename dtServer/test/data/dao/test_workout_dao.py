import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout.workouts_dao import workoutDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_select_recent_user_exercise_library_workouts() : 
    user_id = 1
    exercise_library_id = 1

    data = workoutDao.select_recent_user_exercise_library_workouts(user_id, exercise_library_id)
    
    print(len(data))
    print(data)

def test_get_recent_by_equipment() : 
    user_id = 1
    equipment_id = 11
    res = workoutDao.get_recent_by_equipment(user_id, equipment_id)
    print(res)

def test_get_most_recent_by_equipment() : 
    user_id = 1
    equipment_id = 11
    res = workoutDao.get_most_recent_by_equipment(user_id, equipment_id)
    print(res)

def test_get_recent_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1
    res = workoutDao.get_recent_by_exercise_library(user_id, exercise_library_id)
    print(res)

def test_get_most_recent_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1
    res = workoutDao.get_most_recent_by_exercise_library(user_id, exercise_library_id)
    print(res)

def test_get_recent_by_body_part() : 
    user_id = 1
    body_part_id = 4
    res = workoutDao.get_recent_by_body_part(user_id, body_part_id)
    print(res)

def test_get_most_recent_by_body_part() : 
    user_id = 1
    body_part_id = 4
    res = workoutDao.get_most_recent_by_body_part(user_id, body_part_id)
    print(res)

test_select_recent_user_exercise_library_workouts()
test_get_recent_by_equipment()
test_get_most_recent_by_equipment()
test_get_recent_by_exercise_library()
test_get_most_recent_by_exercise_library()
test_get_recent_by_body_part()
test_get_most_recent_by_body_part()