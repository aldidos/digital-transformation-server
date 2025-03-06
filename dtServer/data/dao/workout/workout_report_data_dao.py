from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.workout.workout_set_dao import workoutSetDao
from dtServer.data.dao.workout.workout_metrics_dao import workoutMetricDao
from dtServer.data.dao.workout.workouts_dao import workoutDao
from dtServer.data.dao.workout.workout_sessions_dao import workoutSessionDao

class WorkoutReportDao :     
    
    def get_workout_set_data(self, workout_set_id) : 
        with db_proxy.atomic() :
            workoutset = workoutSetDao.get_by_id(workout_set_id)
            return self.get_workout_set_metric_data(workoutset)

    def get_recent_set_data_by_equipment(self, user_id, equipment_id, set) : 
        with db_proxy.atomic() : 
            workoutset = workoutSetDao.get_recent_by_equipment(user_id, equipment_id, set)
            return self.get_workout_set_metric_data(workoutset)
        
    def get_recent_set_data_by_bodypart(self, user_id, body_part_id, set) : 
        with db_proxy.atomic() : 
            workoutset = workoutSetDao.get_recent_by_bodypart(user_id, body_part_id, set)
            return self.get_workout_set_metric_data(workoutset)
    
    def get_recent_set_data_by_exercise_library(self, user_id, exercise_library_id, set) : 
        with db_proxy.atomic() : 
            workoutset = workoutSetDao.get_recent_by_exerciselibrary(user_id, exercise_library_id, set)
            return self.get_workout_set_metric_data(workoutset)   
    
    def get_recent_workout_data_by_exercise(self, user_id, exercise_library_id) : 
        with db_proxy.atomic() : 
            workouts = workoutDao.get_recent_by_exercise_library(user_id, exercise_library_id)
            return self.get_workouts_metrics(workouts)            
        
    def get_recent_workout_data_by_body_part(self, user_id, body_part_id) : 
        with db_proxy.atomic() : 
            workouts = workoutDao.get_recent_by_body_part(user_id, body_part_id)
            return self.get_workouts_metrics(workouts)            
        
    def get_recent_workout_data_by_equipment(self, user_id, equipment_id) : 
        with db_proxy.atomic() : 
            workouts = workoutDao.get_recent_by_equipment(user_id, equipment_id)
            return self.get_workouts_metrics(workouts) 
        
    def get_workouts_metrics(self, workouts) : 
        workout_ids = [ d['id'] for d in workouts ]

        workout_metrics = workoutMetricDao.select_by_workouts(workout_ids)
        return workout_metrics 
        
    def get_workout_sessions_by_dateperiod(self, user_id, from_date, to_date) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_by_date_period(user_id, from_date, to_date)
            return workout_metrics
        
    def get_workout_data(self, workout_id) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_by_workout_id(workout_id)
            return workout_metrics

    def get_workoutsession_data(self, workout_session_id) : 
        with db_proxy.atomic() : 
            workout_metrics = workoutMetricDao.select_by_workout_session_id(workout_session_id)
            return workout_metrics
        
    def get_workout_set_metric_data(self, workoutset) : 
        if not workoutset : 
            return None, None
        
        workout_set_id = workoutset['id']
        workout_id = workoutset['workout']['id']       
        workout_metric = workoutMetricDao.select_by_workout_and_workoutset_id(workout_id, workout_set_id)            
        return workoutset, workout_metric
    
workoutReportDao = WorkoutReportDao()