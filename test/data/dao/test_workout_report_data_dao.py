import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout_report_data_dao import workoutReportDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_get_recent_set_data() : 
    user_id = 1
    exercise_library_id = 1
    set_num = 1
    
    data = workoutReportDao.get_recent_set_data(user_id, exercise_library_id, set_num)
    print(data)

def test_get_recent_workout_data_by_user_and_exercise() : 
    user_id = 1
    exercise_library_id = 1
    
    data = workoutReportDao.get_recent_workout_data_by_user_and_exercise(user_id, exercise_library_id)
    print(data)

def test_get_set_data() : 
    workout_id = 1
    workout_set_id = 1

    data = workoutReportDao.get_set_data(workout_id, workout_set_id)
    print(data)

def test_get_workout_data() :
    workout_id = 1
    
    data = workoutReportDao.get_workout_data(workout_id)
    print(data)

def test_get_workout_sessions_by_dateperiod() : 
    user_id = 1
    from_date = '2025-01-01'
    to_date = '2025-03-01'
    
    data = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
    print(data)

def test_get_workoutsession_data() : 
    workout_session_id = 1
    
    data = workoutReportDao.get_workoutsession_data(workout_session_id)
    print(data)

if __name__ == '__main__' : 
    test_get_recent_set_data()
    test_get_recent_workout_data_by_user_and_exercise()
    test_get_set_data()
    test_get_workout_data()
    test_get_workout_sessions_by_dateperiod()
    test_get_workoutsession_data()