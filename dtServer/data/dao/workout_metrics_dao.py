from peewee import Select
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_metrics import WorkoutMetrics, db_proxy
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart
from dtServer.data.model.user import User
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutMetricsDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutMetrics, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            list_ids = []
            for data in list_data : 
                id = WorkoutMetrics.insert(data).execute()
                list_ids.append(id)
            return list_ids
    
    def insert(self, data) : 
        return WorkoutMetrics.insert(data).execute()
    
    def select(self, user_id, from_date, to_date ) :         
        q = WorkoutMetrics.select( WorkoutSessions.id.alias('workout_session'), WorkoutSessions.date, Workouts.completed_sets, 
                                  Workouts.start_time.alias('workout_start_time'), Workouts.end_time.alias('workout_end_time'), 
                                  ExerciseLibrary.name.alias('exercise_library'), BodyPart.name.alias('body_part'),
                                  WorkoutMetrics.rep, WorkoutMetrics.peak_velocity_con, WorkoutMetrics.mean_velocity_con, WorkoutMetrics.peak_power_con, WorkoutMetrics.mean_power_con, 
                                  WorkoutMetrics.peak_foce_con, WorkoutMetrics.mean_foce_con, WorkoutMetrics.peak_acceleration_con, WorkoutMetrics.mean_acceleration_con, 
                                  WorkoutMetrics.peak_velocity_ecc, WorkoutMetrics.mean_velocity_ecc, WorkoutMetrics.peak_power_ecc, WorkoutMetrics.mean_power_ecc, WorkoutMetrics.peak_foce_ecc, WorkoutMetrics.mean_foce_ecc, WorkoutMetrics.peak_acceleration_ecc, WorkoutMetrics.mean_acceleration_ecc, WorkoutMetrics.rep_duration_con, WorkoutMetrics.rep_duration_ecc, WorkoutMetrics.top_stay_duration, WorkoutMetrics.bottom_stay_duration, WorkoutMetrics.rep_duration, WorkoutMetrics.RSI, WorkoutMetrics.RFD
                                            ).join(WorkoutSet)\
            .join(Workouts)\
            .join(ExerciseLibrary)\
            .join(ExerciseLibBodyPart)\
            .join(BodyPart)\
            .join_from(Workouts, WorkoutSessions)\
            .join_from(WorkoutSessions, User)\
            .where(User.id == user_id, WorkoutSessions.is_completed == True, WorkoutSessions.date.between( from_date, to_date) ) 
        list_data = [ row for row in q.dicts()]
        return list_data  
    
workoutMetricDao = WorkoutMetricsDao()
