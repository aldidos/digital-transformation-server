from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart, model_to_dict_or_none, BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibBodyPartDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(ExerciseLibBodyPart, data) )
    
    def insert(self, exercise_library, body_part) : 
        data = {
            'exercise_library' : exercise_library, 
            'body_part' : body_part
        }
        self.save(data)

    def select_by_exercise_library_id(self, exercise_library_id)  :
        q = ExerciseLibBodyPart.select(BodyPart).join(BodyPart).where(ExerciseLibBodyPart.exercise_library == exercise_library_id)
        return [row for row in q.dicts()]

    def select_all(self) : 
        q = ExerciseLibBodyPart.select()
        list_data = [ model_to_dict(row) for row in q ]
        return list_data

    def get_by_exercise_library_id_and_body_part_id(self, exercise_library_id : int, body_part_id : int) : 
        model = ExerciseLibBodyPart.select().where(ExerciseLibBodyPart.exercise_library == exercise_library_id, ExerciseLibBodyPart.body_part == body_part_id).get()
        return model_to_dict_or_none(model)

    def get_by_exercise_library(self, exercise_library_id : int) : 
        q = ExerciseLibBodyPart.select().where( ExerciseLibBodyPart.exercise_library == exercise_library_id )
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def get_by_body_part(self, body_part_id : int) : 
        q = ExerciseLibBodyPart.select().where( ExerciseLibBodyPart.body_part == body_part_id )
        list_data = [model_to_dict(row) for row in q]
        return list_data
    
exerciseLibBodyPartDao = ExerciseLibBodyPartDao()