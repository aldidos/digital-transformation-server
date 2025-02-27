from dtServer.data.dao.base_dao import BaseDAO, dict_to_model, model_to_dict
from dtServer.data.model.ormworkout.ormworkout_exerciselib import ORMWorkoutExerciseLibrary

class ORMWorkoutExerciseLibraryDAO(BaseDAO) : 

    def save(self, ormworkout_id, exercise_library_id) : 
        data = {
            'ormworkout' : ormworkout_id, 
            'exercise_library' : exercise_library_id
        }
        model = dict_to_model(ORMWorkoutExerciseLibrary, data)
        return self.save_model( model )
    
ormworkoutExerciseLibraryDao = ORMWorkoutExerciseLibraryDAO()