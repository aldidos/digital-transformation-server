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
    
    def make_select_query_session_level(self) : 
        q = WorkoutMetrics.select( 
                                  Workouts.completed_sets, Workouts.start_time.alias('workout_start_time'), Workouts.end_time.alias('workout_end_time'), 
                                  ExerciseLibrary.name.alias('exercise_library'), 
                                  WorkoutSet.set, WorkoutSet.weight, WorkoutSet.total_reps, WorkoutSet.set_start_time, WorkoutSet.set_end_time, WorkoutSet.res_start_time, WorkoutSet.res_end_time, 
                                  WorkoutMetrics.rep, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.peak_force, WorkoutMetrics.mean_force,
                                  WorkoutMetrics.peak_velocity_con, WorkoutMetrics.mean_velocity_con, WorkoutMetrics.peak_power_con, WorkoutMetrics.mean_power_con, 
                                  WorkoutMetrics.peak_force_con, WorkoutMetrics.mean_force_con, WorkoutMetrics.peak_acceleration_con, WorkoutMetrics.mean_acceleration_con, 
                                  WorkoutMetrics.peak_velocity_ecc, WorkoutMetrics.mean_velocity_ecc, WorkoutMetrics.peak_power_ecc, WorkoutMetrics.mean_power_ecc, 
                                  WorkoutMetrics.peak_force_ecc, WorkoutMetrics.mean_force_ecc, WorkoutMetrics.peak_acceleration_ecc, WorkoutMetrics.mean_acceleration_ecc, 
                                  WorkoutMetrics.rep_duration_con, WorkoutMetrics.rep_duration_ecc, WorkoutMetrics.top_stay_duration, WorkoutMetrics.bottom_stay_duration, 
                                  WorkoutMetrics.rep_duration, WorkoutMetrics.RSI, WorkoutMetrics.RFD
                                            )\
            .join(WorkoutSet)\
            .join(Workouts)\
            .join(ExerciseLibrary)\
            .join_from(Workouts, WorkoutSessions)\
            .join_from(WorkoutSessions, User)\
        
        return q
    
    def make_select_query_workout_level(self) : 
        q = WorkoutMetrics.select( 
                                WorkoutSet.set, WorkoutSet.weight, WorkoutSet.total_reps, WorkoutSet.set_start_time, WorkoutSet.set_end_time, WorkoutSet.res_start_time, WorkoutSet.res_end_time, 
                                WorkoutMetrics.rep, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.peak_force, WorkoutMetrics.mean_force,
                                WorkoutMetrics.peak_velocity_con, WorkoutMetrics.mean_velocity_con, WorkoutMetrics.peak_power_con, WorkoutMetrics.mean_power_con, 
                                WorkoutMetrics.peak_force_con, WorkoutMetrics.mean_force_con, WorkoutMetrics.peak_acceleration_con, WorkoutMetrics.mean_acceleration_con, 
                                WorkoutMetrics.peak_velocity_ecc, WorkoutMetrics.mean_velocity_ecc, WorkoutMetrics.peak_power_ecc, WorkoutMetrics.mean_power_ecc, 
                                WorkoutMetrics.peak_force_ecc, WorkoutMetrics.mean_force_ecc, WorkoutMetrics.peak_acceleration_ecc, WorkoutMetrics.mean_acceleration_ecc, 
                                WorkoutMetrics.rep_duration_con, WorkoutMetrics.rep_duration_ecc, WorkoutMetrics.top_stay_duration, WorkoutMetrics.bottom_stay_duration, 
                                WorkoutMetrics.rep_duration, WorkoutMetrics.RSI, WorkoutMetrics.RFD)\
                                .join(WorkoutSet)\
                                .join(Workouts)
        
        return q
    
    def make_select_query_workout_set_level(self) : 
        q = WorkoutMetrics.select(                                
                                WorkoutMetrics.rep, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.peak_force, WorkoutMetrics.mean_force,
                                WorkoutMetrics.peak_velocity_con, WorkoutMetrics.mean_velocity_con, WorkoutMetrics.peak_power_con, WorkoutMetrics.mean_power_con, 
                                WorkoutMetrics.peak_force_con, WorkoutMetrics.mean_force_con, WorkoutMetrics.peak_acceleration_con, WorkoutMetrics.mean_acceleration_con, 
                                WorkoutMetrics.peak_velocity_ecc, WorkoutMetrics.mean_velocity_ecc, WorkoutMetrics.peak_power_ecc, WorkoutMetrics.mean_power_ecc, 
                                WorkoutMetrics.peak_force_ecc, WorkoutMetrics.mean_force_ecc, WorkoutMetrics.peak_acceleration_ecc, WorkoutMetrics.mean_acceleration_ecc, 
                                WorkoutMetrics.rep_duration_con, WorkoutMetrics.rep_duration_ecc, WorkoutMetrics.top_stay_duration, WorkoutMetrics.bottom_stay_duration, 
                                WorkoutMetrics.rep_duration, WorkoutMetrics.RSI, WorkoutMetrics.RFD)\
                                .join(WorkoutSet)\
                                .join(Workouts)
        
        return q

    
    def select_by_user_and_dateperiod(self, user_id, from_date, to_date ) : 
        q = self.make_select_query_session_level()
        q = q.where(User.id == user_id, WorkoutSessions.is_completed == True, WorkoutSessions.date.between( from_date, to_date) )

        list_data = [ row for row in q.dicts()]
        return list_data  
    
    def select_workout_session_level_data(self, workout_session_id ) : 
        q = self.make_select_query_session_level()
        q = q.where( WorkoutSessions.id == workout_session_id )

        list_data = [ row for row in q.dicts()]
        return list_data  
    
    def select_woekout_level_data(self, workout_id) : 
        q = self.make_select_query_workout_level()
        q = q.where(Workouts.id == workout_id)

        list_data = [ row for row in q.dicts()]
        return list_data  

    def select_workoutset_level_data(self, workout_id, workoutset_id) : 
        q = self.make_select_query_workout_set_level()
        q = q.where(Workouts.id == workout_id, WorkoutSet.id == workoutset_id)

        list_data = [ row for row in q.dicts()]
        return list_data

workoutMetricDao = WorkoutMetricsDao()
