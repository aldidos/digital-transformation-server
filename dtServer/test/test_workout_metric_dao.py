import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
import pandas as pd

conn = make_database_connection()
db_proxy.initialize(conn)

def test_select_workout_session_level_data() : 
    workout_sessions_id = 1
    data = workoutMetricDao.select_workout_session_level_data(workout_sessions_id)
    print(data)

def test_select_by_user_and_dateperiod() : 
    user_id = 1
    from_date = '2025-01-01'
    to_date = '2025-03-01'

    data = workoutMetricDao.select_by_user_and_dateperiod(user_id, from_date, to_date)
    print(data)

def test_select_workout_level_data() : 
    workout_id = 1
    
    data = workoutMetricDao.select_workout_level_data(workout_id)
    print(data)

def test_select_workoutset_level_data() : 
    workout_id = 1
    workout_set_id = 2
    
    data = workoutMetricDao.select_workoutset_level_data(workout_id, workout_set_id)
    print(data)

def test_select_workout_sets_data() : 
    workout_id = 1
    
    data = workoutMetricDao.select_workout_sets_data(workout_id)
    print(data)    

if __name__ == '__main__' : 
    # test_select_workout_session_level_data()
    # test_select_by_user_and_dateperiod() 
    # test_select_workout_level_data() 
    # test_select_workoutset_level_data()
    test_select_workout_sets_data()