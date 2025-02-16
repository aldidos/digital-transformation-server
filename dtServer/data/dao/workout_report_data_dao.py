from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.workout_set_dao import workoutSetDao
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.dao.workouts_dao import workoutDao
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao

class WorkoutReportDao : 
    
    def get_recent_set_data(self, user_id, exercise_library_id, set) : 
        with db_proxy.atomic() : 
            recent_workoutset = workoutSetDao.get_recent_by_exerciselibrary(user_id, exercise_library_id, set)

            if not recent_workoutset : 
                return None, None 

            workout_set_id = recent_workoutset['id']
            workout_id = recent_workoutset['workout']['id']

            return self.get_set_data(workout_id, workout_set_id)
    
    def get_set_data(self, workout_id, workout_set_id) : 
        with db_proxy.atomic() : 
            workout_set = workoutSetDao.get_by_id(workout_set_id)
            if not workout_set : 
                return None, None      
            workout_metric = workoutMetricDao.select_workoutset_level_data(workout_id, workout_set_id)
            return workout_set, workout_metric
    
    def get_workout_data(self, workout_id) : 
        with db_proxy.atomic() : 
            workout = workoutDao.select_by_id(workout_id)
            if not workout : 
                return None, None      
            workout_metrics = workoutMetricDao.select_workout_level_data(workout_id)
            return workout, workout_metrics

    def get_workoutsession_data(self, workout_session_id) : 
        with db_proxy.atomic() : 
            workout_session = workoutSessionDao.select_by_id(workout_session_id)
            if not workout_session : 
                return None, None
            workout_metrics = workoutMetricDao.select_workout_session_level_data(workout_session_id)
            return workout_session, workout_metrics
        
    def get_recent_workout_data_by_user_and_exercise(self, user_id, exercise_library_id) : 
        with db_proxy.atomic() : 
            workouts = workoutDao.select_recent_user_exercise_library_workouts(user_id, exercise_library_id)
            list = []
            for workout in workouts : 
                workout_id = workout['workout']
                workout_metrics = workoutMetricDao.select_workout_level_data(workout_id)
                
                list.append({
                    'workout' : workout, 
                    'workout_metrics' : workout_metrics
                })
            return list
        
    def get_workout_sessions_by_dateperiod(self, user_id, from_date, to_date) : 
        with db_proxy.atomic() : 
            list_workout_sessions_dataset = []
            workout_sessions = workoutSessionDao.select_by_user_and_date_period(user_id, from_date, to_date)
            for workout_session in workout_sessions : 
                workout_session_id = workout_session['id']
                workout_session_metric = workoutMetricDao.select_workout_session_level_data(workout_session_id)
                list_workout_sessions_dataset.append({
                    'workout_session' : workout_session, 
                    'workout_session_metric' : workout_session_metric
                })
            return list_workout_sessions_dataset
    
workoutReportDao = WorkoutReportDao()
