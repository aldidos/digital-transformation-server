from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.weight_metric import WeightMetric, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class WeightMetricDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WeightMetric, data) )
    

weightMetricDao = WeightMetricDao()