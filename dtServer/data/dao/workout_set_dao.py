from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_set import WorkoutSet
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutSetDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutSet, data) )
    
    def insert(self, data) : 
        return WorkoutSet.insert(data).execute()
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            WorkoutSet.insert_many(list_data).execute() 
        
    
workoutSetDao = WorkoutSetDao()