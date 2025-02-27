from dtServer.data.dao.base_dao import BaseDAO, dict_to_model, model_to_dict
from dtServer.data.model.ormworkout.ormworkout_bodypart import ORMWorkoutBodypart

class ORMWorkoutBodypartDAO(BaseDAO) : 

    def save(self, ormworkout_id, body_part_id) : 
        data = {
            'ormworkout' : ormworkout_id, 
            'body_part' : body_part_id
        }
        model = dict_to_model(ORMWorkoutBodypart, data)
        return self.save_model( model )
    
ormworkoutBodypartDao = ORMWorkoutBodypartDAO()