from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workouts import Workouts, db_proxy, model_to_dict_or_none
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutsDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(Workouts, data) )
    
    def select_by_id(self, id : int) : 
        workout =  Workouts.get_or_none(Workouts.id == id)    
        return model_to_dict_or_none(workout)

    def select_by_workout_session(self, workout_session_id : int) : 
        q = Workouts.select().where( Workouts.workout_session == workout_session_id )
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def select_by_user_and_date_period(self, user_id, from_date, to_date) : 
        q = Workouts.select( ExerciseLibrary.name.alias('exercise_library_name'), Workouts.completed_sets, Workouts.start_time, Workouts.end_time)\
            .join(WorkoutSessions)\
            .join(User)\
            .join_from(Workouts, ExerciseLibrary)\
            .where(WorkoutSessions.is_completed == True, User.id == user_id,  WorkoutSessions.date.between(from_date, to_date))
        
        return [ row for row in q.dicts() ]
    
    def insert(self, data) : 
        return Workouts.insert(data).execute()

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            Workouts.insert_many(list_data).execute()
    
workoutDao = WorkoutsDao()