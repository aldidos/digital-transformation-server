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

test_select_recent_user_exercise_library_workouts()