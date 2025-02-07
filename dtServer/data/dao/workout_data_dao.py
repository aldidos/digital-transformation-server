from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.dao.workouts_dao import workoutDao, Workouts
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.body_part import BodyPart
from dtServer.data.model.user import User
from dtServer.data.model.workout_data import WorkoutData
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutDataDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutData, data) )
    
    def create( self, user_id, workout_session_id, exercise_lib_id, bodypart_id, workout_metric_id ) : 
         return {
              'user' : user_id, 
              'workout_session' : workout_session_id, 
              'exercise_library_id' : exercise_lib_id, 
              'body_part' : bodypart_id, 
              'workout_metric' : workout_metric_id 
         }
    
    def insert_many(self, user_id, workout_session_id, workout_id, workout_metric_ids) : 
        with db_proxy.atomic() :             
            workout_dict = workoutDao.select_by_id(workout_id) 
            exercise_lib_dict = workout_dict['exercise_library']
            exerciselib_bodyparts = exerciseLibBodyPartDao.get_by_exercise_library(exercise_lib_dict['id'])

            list_data = []

            for exercise_bodypart in exerciselib_bodyparts : 
                 bodypart_id = exercise_bodypart['body_part']['id']

                 for workout_metric_id in workout_metric_ids : 
                    list_data.append( self.create(user_id, workout_session_id, exercise_lib_dict['id'], bodypart_id, workout_metric_id ) ) 

            WorkoutData.insert_many(list_data).execute()

    def select(self, user_id, from_date, to_date) : 
        q = WorkoutData.select(WorkoutSessions.date,\
                            ExerciseLibrary.name.alias('exercise_library_name'),\
                            BodyPart.name.alias('body_part_name'),\
                            WorkoutMetrics.set, WorkoutMetrics.rep, WorkoutMetrics.weight, WorkoutMetrics.volume,\
                            WorkoutMetrics.peak_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_velocity,\
                            WorkoutMetrics.mean_power, WorkoutMetrics.power, WorkoutMetrics.height,\
                            WorkoutMetrics.workout.id.alias('workout_id'), WorkoutMetrics.workout.start_time, WorkoutMetrics.workout.end_time)\
            .join(User)\
            .join_from(WorkoutData, WorkoutSessions)\
            .join_from(WorkoutData, ExerciseLibrary)\
            .join_from(WorkoutData, BodyPart)\
            .join_from(WorkoutData, WorkoutMetrics)\
            .join(Workouts)\
            .where(WorkoutSessions.is_completed == True, WorkoutSessions.user == user_id, WorkoutSessions.date.between(from_date, to_date))
        return [ row for row in q.dicts()]

workoutDataDao = WorkoutDataDao()
