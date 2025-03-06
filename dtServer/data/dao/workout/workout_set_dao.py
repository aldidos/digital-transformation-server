from dtServer.data.model.base_model import db_proxy, model_to_dict_or_none
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout.workout_sessions import WorkoutSessions
from dtServer.data.model.workout.workouts import Workouts
from dtServer.data.model.workout.workout_set import WorkoutSet
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.workout_exerciselib import WorkoutExerciseLib
from dtServer.data.model.user.user import User
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.workout_body_part import WorkoutBodypart
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutSetDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutSet, data) )
    
    def insert(self, data) : 
        return WorkoutSet.insert(data).execute()
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            WorkoutSet.insert_many(list_data).execute() 

    def get_recent_by_exerciselibrary(self, user_id, exercise_library_id, set) :
        recent_workout_set = WorkoutSet.select( WorkoutSet )\
                            .join(Workouts)\
                            .join(WorkoutExerciseLib)\
                            .join(ExerciseLibrary)\
                            .join_from(Workouts, WorkoutSessions)\
                            .join(User)\
                            .where( User.id == user_id, WorkoutSessions.is_completed == True, ExerciseLibrary.id == exercise_library_id, WorkoutSet.set == set )\
                            .order_by(WorkoutSessions.date.desc()).get_or_none()
        
        return model_to_dict_or_none(recent_workout_set )
    
    def get_recent_by_equipment(self, user_id, equipment_id, set) :
        recent_workout_set = WorkoutSet.select( WorkoutSet )\
                            .join(Workouts)\
                            .join(Equipment)\
                            .join_from(Workouts, WorkoutSessions)\
                            .join(User)\
                            .where( User.id == user_id, WorkoutSessions.is_completed == True, Equipment.id == equipment_id, WorkoutSet.set == set )\
                            .order_by(WorkoutSessions.date.desc()).get_or_none()
        
        return model_to_dict_or_none(recent_workout_set )
    
    def get_recent_by_bodypart(self, user_id, body_part_id, set) :
        recent_workout_set = WorkoutSet.select( WorkoutSet )\
                            .join(Workouts)\
                            .join(WorkoutBodypart)\
                            .join(BodyPart)\
                            .join_from(Workouts, WorkoutSessions)\
                            .join(User)\
                            .where( User.id == user_id, WorkoutSessions.is_completed == True, BodyPart.id == body_part_id, WorkoutSet.set == set )\
                            .order_by(WorkoutSessions.date.desc()).get_or_none()
        
        return model_to_dict_or_none(recent_workout_set )
    
    def get_by_id(self, id) : 
        workout_set = WorkoutSet.get_or_none(WorkoutSet.id == id)
        return model_to_dict_or_none(workout_set)    
    
workoutSetDao = WorkoutSetDao()