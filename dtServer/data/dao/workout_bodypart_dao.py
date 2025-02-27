from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout.workout_metrics import db_proxy
from dtServer.data.model.workout_body_part import WorkoutBodypart
from dtServer.data.model.workout.workouts import Workouts
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutBodyPartDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutBodypart, data) )
    
    def create(self, workout_id, body_part_id) : 
        return self.save( {
            'workout' : workout_id, 
            'body_part' : body_part_id
        })
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            list_ids = []
            for data in list_data : 
                id = WorkoutBodypart.insert(data).execute()
                list_ids.append(id)
            return list_ids
    
    def insert(self, data) : 
        return WorkoutBodypart.insert(data).execute()
    
    def select_bodyparts_by_workout(self, workout_id) : 
        q = WorkoutBodypart.select(BodyPart)\
                                .join(Workouts)\
                                .join_from(WorkoutBodypart, BodyPart)\
                                .where(Workouts.id == workout_id)
                
        return [ d for d in q.dicts() ]

workoutBodypartDao = WorkoutBodyPartDao()
