import pandas as pd
from datetime import datetime, timedelta, time, date

today = date.today()
y = today.year
m = today.month
d = today.day
H = 13
M = 0
S = 0 

def create_test_workout_metric_dataset(rep) : 
    m_value = 0.2
    time_duration = time(0,0,30)
    
    keys = ['rep', 'mean_velocity', 'peak_velocity', 'mean_power', 'peak_power', 'rep_duration_con', 'rep_duration_ecc','top_stay_duration','bottom_stay_duration','rep_duration']
    values = [rep, m_value, m_value, m_value, m_value, time_duration, time_duration, time_duration, time_duration, time_duration ]
    data = []
    for i in range(len(keys)) : 
        k = keys[i]        
        v = values[i]
        data.append( (k,v) )
    return data

def create_test_workout_set_dataset(num_set : int, num_reps : int, date : date ) :    
    start_time = datetime(date.year, date.month, date.day, H, M, S)
    end_time = datetime(date.year, date.month, date.day, H, M, S + 10)
    weight = 100

    keys = ['set_id', 'set', 'weight', 'total_reps', 'set_start_time', 'set_end_time', 'res_start_time','res_end_time']
    values = [ num_set, num_set, weight, num_reps, start_time, end_time, start_time, end_time ]
    data = []
    for i in range(len(keys)) : 
        k = keys[i]
        v = values[i]
        data.append((k,v))

    return data

def create_test_workout_dataset(workout_id : int, num_set : int, date : date) : 
    start_time = datetime(date.year, date.month, date.day, H, M, S)
    end_time = datetime(date.year, date.month, date.day, H, M, S + 10)
    exercise_library_id = 1
    body_part_id = 1
    exercise_library = 'let pull down'
    body_part = 'boyd_part_1'

    keys = ['workout', 'completed_sets', 'workout_start_time', 'workout_end_time', 'exercise_library_id', 'exercise_library', 'body_part_id','body_part']
    values = [ workout_id, num_set, start_time, end_time, exercise_library_id, exercise_library, body_part_id, body_part ]

    data = []
    for i in range(len(keys)) : 
        k = keys[i]
        v = values[i]
        data.append((k,v))

    return data   

def create_test_workout_session_data(workout_session_id : int, date : date) :     
    keys = ['workout_session', 'date']
    values = [workout_session_id, date]

    data = []
    for i in range(len(keys)) : 
        k = keys[i]
        v = values[i]
        data.append((k,v))

    return data   

def create_test_dataset(n_workout_session = 1, n_workouts = 1, n_sets = 1, n_reps = 3) : 
    dataset = []
    for ws in range(n_workout_session) : 
        ws_id = ws + 1
        date = today + timedelta(days = 1)
        workout_session_data = create_test_workout_session_data(ws_id, date) 
        
        data = []
        data.extend(workout_session_data)

        for w in range(n_workouts) : 
            workout_id = w + 1
            workout_data = create_test_workout_dataset(workout_id, n_sets, date)
            data.extend(workout_data)

            for s in range(n_sets) : 
                workout_set_id = s + 1
                workout_set_data = create_test_workout_set_dataset(workout_set_id, n_reps, date)
                data.extend(workout_set_data)

                for r in range(n_reps) : 
                    rep = r + 1
                    metric_data = create_test_workout_metric_dataset(rep)
                    data.extend(metric_data)
                    
                    dataset.append(dict(data))
    
    df = pd.DataFrame(dataset)

    return df