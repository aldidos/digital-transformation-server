from peewee import Select
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout.workout_metrics import WorkoutMetrics, db_proxy
from dtServer.data.model.workout.workout_sessions import WorkoutSessions
from dtServer.data.model.workout.workouts import Workouts
from dtServer.data.model.workout.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart
from dtServer.data.model.user.user import User
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model
from dtServer.data.dao.query.workout_metric_query_builder import WorkoutMatricQueryBuilder

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
        
    def select_by_date_period(self, user_id, from_date, to_date ) : 
        q = WorkoutMatricQueryBuilder.make_select_query()
        q = q.where(User.id == user_id, WorkoutSessions.is_completed == True, WorkoutSessions.date.between( from_date, to_date) )

        list_data = [ row for row in q.dicts()]
        return list_data  
    
    def select_by_workout_session_id(self, workout_session_id ) : 
        q = WorkoutMatricQueryBuilder.make_select_query()
        q = q.where( WorkoutSessions.id == workout_session_id )

        list_data = [ row for row in q.dicts()]
        return list_data
    
    def select_by_workout_id(self, workout_id) : 
        q = WorkoutMatricQueryBuilder.make_select_query()
        q = q.where(Workouts.id == workout_id)

        list_data = [ row for row in q.dicts()]
        return list_data  
    
    def select_by_workout_and_workoutset_id(self, workout_id, workoutset_id) : 
        q = WorkoutMatricQueryBuilder.make_select_query()
        q = q.where(Workouts.id == workout_id, WorkoutSet.id == workoutset_id)

        list_data = [ row for row in q.dicts()]
        return list_data
        
    def select_by_workouts(self, workout_ids) : 
        q = WorkoutMatricQueryBuilder.make_select_query()
        q = q.where(Workouts.id.in_(workout_ids))

        list_data = [ row for row in q.dicts()]
        return list_data  


workoutMetricDao = WorkoutMetricsDao()
