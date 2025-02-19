import pandas as pd
from datetime import datetime, timedelta, time, date

def create_test_workout_set_dataset() : 
    today = date.today()
    y = today.year
    m = today.month
    d = today.day
    H = 13
    M = 0
    S = 0 

    worout_session_date = date(y, m, d)
    workout = 1
    completed_sets = 3
    start_time = datetime(y,m,d, H, M, S)
    end_time = datetime(y,m,d, H, M, S + 10)    
    m_value = 0.2
    time_duration = time(0,0,30)

    list_data = []
    for rep in range(10) : 
        data = {
            'workout_session' : 1,
            'date' : worout_session_date,
            'workout' : workout,
            'completed_sets' : completed_sets,
            'workout_start_time' : start_time,
            'workout_end_time' : end_time,
            'exercise_library_id' : 1,
            'exercise_library' : 'let pull down',
            'body_part_id' : 1,
            'body_part' : 'part_1',
            'set_id' : 1,
            'set' : 1,
            'weight' : 50,
            'total_reps' : 10,
            'set_start_time' : start_time,
            'set_end_time' : end_time,
            'res_start_time' : start_time,
            'res_end_time' : end_time,
            'rep' : rep,
            'mean_velocity' : m_value,
            'peak_velocity' : m_value,
            'mean_power' : m_value,
            'peak_power' : m_value,
            'rep_duration_con' : time_duration,
            'rep_duration_ecc' : time_duration,
            'top_stay_duration' : time_duration,
            'bottom_stay_duration' : time_duration,
            'rep_duration' : time_duration,
        }
        list_data.append(data)
    
    return pd.DataFrame(list_data)


def create_test_workout_dataset() : 
    today = date.today()
    y = today.year
    m = today.month
    d = today.day
    H = 13
    M = 0
    S = 0 

    worout_session_date = date(y, m, d)
    workout = 1
    completed_sets = 3
    start_time = datetime(y,m,d, H, M, S)
    end_time = datetime(y,m,d, H, M, S + 10)    
    m_value = 0.2
    time_duration = time(0,0,30)
    weights = [50, 80, 100]

    list_data = []

    for set in range(3) : 
        for rep in range(10) : 
            data = {
                'workout_session' : 1,
                'date' : worout_session_date,
                'workout' : workout,
                'completed_sets' : completed_sets,
                'workout_start_time' : start_time,
                'workout_end_time' : end_time,
                'exercise_library_id' : 1,
                'exercise_library' : 'let pull down',
                'body_part_id' : 1,
                'body_part' : 'part_1',
                'set_id' : set,
                'set' : set,
                'weight' : weights[set],
                'total_reps' : 10,
                'set_start_time' : start_time,
                'set_end_time' : end_time,
                'res_start_time' : start_time,
                'res_end_time' : end_time,
                'rep' : rep,
                'mean_velocity' : m_value,
                'peak_velocity' : m_value,
                'mean_power' : m_value,
                'peak_power' : m_value,
                'rep_duration_con' : time_duration,
                'rep_duration_ecc' : time_duration,
                'top_stay_duration' : time_duration,
                'bottom_stay_duration' : time_duration,
                'rep_duration' : time_duration,
            }
            list_data.append(data)
    
    return pd.DataFrame(list_data)