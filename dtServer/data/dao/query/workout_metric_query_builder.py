from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart
from dtServer.data.model.user import User

class WorkoutMatricQueryBuilder : 

    def query_for_set_data() : 
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
    
    def query_for_workout_data() : 
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
    
    def query_for_session_data() : 
        q = WorkoutMetrics.select( 
                                  Workouts.id.alias('workout'), Workouts.completed_sets, Workouts.start_time, Workouts.end_time, 
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
                                .join_from(WorkoutSessions, User)
        return q