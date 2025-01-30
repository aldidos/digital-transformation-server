from dtServer.data.model.exercise_library import save_exercise_library, select_exericse_libraries
from dtServer.data.model.user_exercise_metric import save_user_exercise_metric, select_user_exer_metric, create_user_exercise_metric
from dtServer.data.model.workout_sessions import save_workout_session, create_workout_session, select_workout_session, select_workout_sessions, select_workout_sessions_period
from dtServer.data.model.workouts import save_workout, select_workout, select_workouts
from dtServer.data.model.workout_metrics import save_workout_metric, select_join_with_workout_sessions, insert_multiple_workout_metrics

def post_exercise_library(data) : 
    n = save_exercise_library(data)
    if n > 0 : 
        return True
    return False

def get_exercise_libraries() : 
    return select_exericse_libraries()

def post_user_weight_metric(user_id, exercise_lib_id, weight) : 
    create_user_exercise_metric(user_id, exercise_lib_id, weight)
    return True

def get_user_weight_metric(user_id, exercise_lib_id) :
    select_user_exer_metric(user_id, exercise_lib_id)
    
def patch_user_weight_metric(data) : 
    n = save_user_exercise_metric(data)
    if n > 0 : 
        return True
    return False

def post_user_workout_session(user_id, date, status) : 
    workout_session = create_workout_session(user_id, date, status)
    return workout_session

def get_user_workout_sessions_period(user_id, from_date, to_date) : 
    workout_sessions = select_workout_sessions_period(user_id, from_date, to_date)
    return workout_sessions

def get_user_workout_sessions(user_id, date) : 
    workout_sessions = select_workout_sessions(user_id, date)
    return workout_sessions

def patch_user_workout_session(data) : 
    return save_workout_session(data)

def post_workout(data) : 
    model, result = save_workout(data)    
    return model

def patch_workout(data) : 
    model, result = save_workout(data)
    return result

def get_workouts(workout_session_id) : 
    return select_workouts(workout_session_id)

def put_workout(data) : 
    return save_workout(data)

def get_workout(workout_id) : 
    return select_workout(workout_id)

def post_workout_metric(data) : 
    return save_workout_metric(data)

def post_workout_metrics(list_data) : ####
    insert_multiple_workout_metrics(list_data)

def get_workout_metrics(user_id, from_date, to_date) : 
    return select_join_with_workout_sessions(user_id, from_date, to_date)