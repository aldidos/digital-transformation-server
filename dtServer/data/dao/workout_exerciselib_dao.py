from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout.workout_metrics import db_proxy
from dtServer.data.model.workout_exerciselib import WorkoutExerciseLib
from dtServer.data.model.workout.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutExerciseLibDAO(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutExerciseLib, data) )
    
    def create(self, workout_id, exercise_library_id) : 
        return self.save( {
            'workout' : workout_id, 
            'exercise_library' : exercise_library_id
        })
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            list_ids = []
            for data in list_data : 
                id = WorkoutExerciseLib.insert(data).execute()
                list_ids.append(id)
            return list_ids
    
    def insert(self, data) : 
        return WorkoutExerciseLib.insert(data).execute() 
    
    def select_exerciselibs_by_workout(self, workout_id) : 
        q = WorkoutExerciseLib.select(ExerciseLibrary)\
                                .join(Workouts)\
                                .join_from(WorkoutExerciseLib, ExerciseLibrary)\
                                .where(Workouts.id == workout_id)
                
        return [ d for d in q.dicts() ]


workoutExerciselibDao = WorkoutExerciseLibDAO()
