from dtServer.data.model.base_model import db_proxy, model_to_dict_or_none
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.workout_exerciselib import WorkoutExerciseLib
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutSetDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutSet, data) )
    
    def insert(self, data) : 
        return WorkoutSet.insert(data).execute()
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            WorkoutSet.insert_many(list_data).execute() 

    def get_recent_by_exerciselibrary(self, user_id, exercise_library, set) :             
        recent_workout_set = WorkoutSet.select( WorkoutSet )\
                            .join(Workouts)\
                            .join(WorkoutExerciseLib)\
                            .join(ExerciseLibrary)\
                            .join_from(Workouts, WorkoutSessions)\
                            .join(User)\
                            .where( User.id == user_id, WorkoutSessions.is_completed == True, ExerciseLibrary.id == exercise_library, WorkoutSet.set == set )\
                            .order_by(WorkoutSessions.date.desc(), WorkoutSet.set.desc()).get_or_none()
        
        return model_to_dict_or_none(recent_workout_set )
    
    def get_by_id(self, id) : 
        workout_set = WorkoutSet.get_or_none(WorkoutSet.id == id)
        return model_to_dict_or_none(workout_set)    
    
workoutSetDao = WorkoutSetDao()