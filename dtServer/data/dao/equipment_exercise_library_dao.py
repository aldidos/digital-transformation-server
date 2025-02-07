from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.equipment_exerciselib import EquipmentExerciseLib, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class EquipmentExerciseLibDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(EquipmentExerciseLib, data) )
    
    def get_by_equipment_id(self, equipment_id : int) :
        model = EquipmentExerciseLib.select().where( EquipmentExerciseLib.equipment == equipment_id ).get()
        return model_to_dict_or_none(model)    

    def get_by_exercise_library_id(self, exercise_library_id : int) :
        model = EquipmentExerciseLib.select().where( EquipmentExerciseLib.exercise_library == exercise_library_id ).get()
        return model_to_dict_or_none(model)
    
equipmentExerciseLib = EquipmentExerciseLibDao()