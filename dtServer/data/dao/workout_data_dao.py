from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_data import WorkoutData, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutDataDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutData, data) )