from dtServer.data.model.exercise_library import save_exercise_library, select_exericse_libraries
from dtServer.data.model.user_exercise_metric import save_user_exercise_metric, select_user_exer_metric, create_user_exercise_metric
from dtServer.data.model.workout_sessions import save_workout_session, create_workout_session, select_workout_session, select_workout_sessions, select_workout_sessions_period
from dtServer.data.model.workouts import save_workout, select_workout_by_id, select_workouts
from dtServer.data.model.workout_metrics import save_workout_metric, select_join_with_workout_sessions, insert_multiple_workout_metrics
from dtServer.data.data_converter import model_to_dict_or_none

def post_exercise_library(data) : 
    return save_exercise_library(data)    

def get_exercise_libraries() : 
    return select_exericse_libraries()

def post_user_exercise_weight(data) : 
    return save_user_exercise_metric(data)    

def get_user_exercise_weight(user_id, exercise_lib_id) :
    user_exer_metric = select_user_exer_metric(user_id, exercise_lib_id)
    return model_to_dict_or_none(user_exer_metric)
    
def patch_user_exercise_weight(data) : 
    return save_user_exercise_metric(data)

def post_user_workout_session(data) : 
    return save_workout_session(data)

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
    workout = select_workout_by_id(workout_id)
    return model_to_dict_or_none(workout)

def post_workout_metric(data) : 
    return save_workout_metric(data)

def post_workout_metrics(list_data) : ####
    insert_multiple_workout_metrics(list_data)

def get_workout_metrics(user_id, from_date, to_date) : 
    return select_join_with_workout_sessions(user_id, from_date, to_date)