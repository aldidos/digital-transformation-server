from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.workout.workout_set_dao import workoutSetDao
from dtServer.data.dao.workout.workout_metrics_dao import workoutMetricDao
from dtServer.data.dao.workout.workouts_dao import workoutDao
from dtServer.data.dao.workout.workout_sessions_dao import workoutSessionDao

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
            workout_metric = workoutMetricDao.select_workoutset_level_data(workout_id, workout_set_id)            
            return workout_metric
    
    def get_workout_data(self, workout_id) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_workout_level_data(workout_id)
            return workout_metrics

    def get_workoutsession_data(self, workout_session_id) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_workout_session_level_data(workout_session_id)
            return workout_metrics
        
    def get_recent_workout_data_by_user_and_exercise(self, user_id, exercise_library_id) : 
        with db_proxy.atomic() : 
            workouts = workoutDao.select_recent_user_exercise_library_workouts(user_id, exercise_library_id)

            workout_ids = [ d['workout'] for d in workouts ]

            workout_metrics = workoutMetricDao.select_by_workouts(workout_ids)
            return workout_metrics
        
    def get_workout_sessions_by_dateperiod(self, user_id, from_date, to_date) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_by_user_and_dateperiod(user_id, from_date, to_date)
            return workout_metrics

    
workoutReportDao = WorkoutReportDao()
