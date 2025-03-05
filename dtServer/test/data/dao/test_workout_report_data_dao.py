import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout.workout_report_data_dao import workoutReportDao

conn = make_database_connection()
db_proxy.initialize(conn)

def test_get_recent_set_data_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1
    set_num = 1
    
    data = workoutReportDao.get_recent_set_data_by_exercise_library(user_id, exercise_library_id, set_num)
    print(data)

def test_get_recent_set_data_by_body_part() : 
    user_id = 1
    body_part_id = 4
    set_num = 1
    
    data = workoutReportDao.get_recent_set_data_by_bodypart(user_id, body_part_id, set_num)
    print(data)

def test_get_recent_set_data_by_equipment() : 
    user_id = 1
    equipment_id = 11
    set_num = 1
    
    data = workoutReportDao.get_recent_set_data_by_equipment(user_id, equipment_id, set_num)
    print(data)

def test_get_recent_workout_data_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1
    
    data = workoutReportDao.get_recent_workout_data_by_exercise(user_id, exercise_library_id)
    print(data)

def test_get_recent_workout_data_by_body_part() : 
    user_id = 1
    body_part_id = 4
    
    data = workoutReportDao.get_recent_workout_data_by_body_part(user_id, body_part_id)
    print(data)

def test_get_recent_workout_data_by_equipment() : 
    user_id = 1
    equipment_id = 11
    
    data = workoutReportDao.get_recent_workout_data_by_equipment(user_id, equipment_id)
    print(data)

def test_get_set_data() : 
    workoutset = {
        'id' : 1, 
        'workout' : {
            'id' : 1
        }
    }

    data = workoutReportDao.get_workout_set_metric_data(workoutset)
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
    test_get_recent_set_data_by_exercise_library()
    test_get_recent_set_data_by_body_part()
    test_get_recent_set_data_by_equipment()
    test_get_recent_workout_data_by_exercise_library()
    test_get_recent_workout_data_by_body_part()
    test_get_recent_workout_data_by_equipment()
    test_get_set_data()
    test_get_workout_data()
    test_get_workout_sessions_by_dateperiod()
    test_get_workoutsession_data()