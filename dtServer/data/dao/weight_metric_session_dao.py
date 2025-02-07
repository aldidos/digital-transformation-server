from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.weight_metric_session import WeightMetricSession, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class WeightMetricSessionDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WeightMetricSession, data) )
    
    def select_by_id(self, id) : 
        weight_session = WeightMetricSession.get_by_id(id)
        return model_to_dict_or_none(weight_session)
    
    def select_by_user_and_exercise_library(self, user : int, exercise_library : int) : 
        user_exercise_metric = WeightMetricSession.get_or_none(WeightMetricSession.user == user and WeightMetricSession.exercise_library == exercise_library)
        return model_to_dict_or_none(user_exercise_metric)

    def select_by_user(self, user : int) : 
        q = WeightMetricSession.select().where(WeightMetricSession.user == user)
        list_data = [model_to_dict(row) for row in q]
        return list_data
    
    def select_by_date_period(self, from_date, to_date) : 
        q = WeightMetricSession.select().where(WeightMetricSession.date.between(from_date, to_date ))
        list_data = [model_to_dict(row) for row in q]
        return list_data

    
weightMetricSession = WeightMetricSessionDao()