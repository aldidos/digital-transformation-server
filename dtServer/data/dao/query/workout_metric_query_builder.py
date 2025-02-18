from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.body_part import BodyPart
from dtServer.data.model.workout_exerciselib import WorkoutExerciseLib
from dtServer.data.model.workout_body_part import WorkoutBodypart
from dtServer.data.model.user import User
from dtServer.data.model.equipment import Equipment

class WorkoutMatricQueryBuilder : 

    def make_select_query() : 
        q = WorkoutMetrics.select( 
                                WorkoutSessions.id.alias('workout_session'), WorkoutSessions.date, 
                                Workouts.id.alias('workout'), Workouts.completed_sets, Workouts.start_time.alias('workout_start_time'), Workouts.end_time.alias('workout_end_time'), 
                                ExerciseLibrary.id.alias('exercise_library_id'), ExerciseLibrary.name.alias('exercise_library'), BodyPart.id.alias('body_part_id'), BodyPart.name.alias('body_part'),
                                WorkoutSet.id.alias('set_id'), WorkoutSet.set, WorkoutSet.weight, WorkoutSet.total_reps, WorkoutSet.set_start_time, WorkoutSet.set_end_time, 
                                WorkoutSet.res_start_time, WorkoutSet.res_end_time,
                                WorkoutMetrics.rep, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.peak_force, WorkoutMetrics.mean_force,
                                WorkoutMetrics.peak_velocity_con, WorkoutMetrics.mean_velocity_con, WorkoutMetrics.peak_power_con, WorkoutMetrics.mean_power_con, 
                                WorkoutMetrics.peak_force_con, WorkoutMetrics.mean_force_con, WorkoutMetrics.peak_acceleration_con, WorkoutMetrics.mean_acceleration_con, 
                                WorkoutMetrics.peak_velocity_ecc, WorkoutMetrics.mean_velocity_ecc, WorkoutMetrics.peak_power_ecc, WorkoutMetrics.mean_power_ecc, 
                                WorkoutMetrics.peak_force_ecc, WorkoutMetrics.mean_force_ecc, WorkoutMetrics.peak_acceleration_ecc, WorkoutMetrics.mean_acceleration_ecc, 
                                WorkoutMetrics.rep_duration_con, WorkoutMetrics.rep_duration_ecc, WorkoutMetrics.top_stay_duration, WorkoutMetrics.bottom_stay_duration, 
                                WorkoutMetrics.rep_duration, WorkoutMetrics.RSI, WorkoutMetrics.RFD)
        q = q.join(WorkoutSet)\
            .join(Workouts)\
            .join_from(Workouts, WorkoutExerciseLib)\
            .join(ExerciseLibrary)\
            .join_from(Workouts, WorkoutBodypart)\
            .join(BodyPart)\
            .join_from(Workouts, WorkoutSessions)\
            .join_from(WorkoutSessions, User)
        
        return q