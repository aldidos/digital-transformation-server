from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.base_dao import BaseDAO, dict_to_model, model_to_dict
from dtServer.data.model.ormworkout.ormworkout_metric import ORMWorkoutMetric
from dtServer.data.model.ormworkout.ormworkout import ORMWorkout
from dtServer.data.model.user.user import User
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.exercise_library import ExerciseLibrary

class ORMWorkoutMetricDAO(BaseDAO) :     
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            ORMWorkoutMetric.insert_many(list_data).execute()

    def select_by_ormworkout_id(self, ormworkout_id) : 
        q = ORMWorkoutMetric.select().where( ORMWorkoutMetric.ormworkout == ormworkout_id )
        return [ row for row in q.dicts() ]
    
    def select_recent_by_exerciselibrary(self, user_id, exercise_library_id) : 
        q = ORMWorkoutMetric.select( ORMWorkoutMetric.ormworkout, ORMWorkoutMetric.weight, ORMWorkoutMetric.mean_velocity, ORMWorkoutMetric.mean_power )\
            .join(ORMWorkout)\
            .join(User)\
            .join_from(ORMWorkout, Equipment)\
            .join(ExerciseLibrary)\
            .where(User.id == user_id, ExerciseLibrary.id == exercise_library_id)\
            .order_by(ORMWorkout.date.desc())\
            .limit(7)        
        return [ row for row in q.dicts() ] 

ormWorkoutMetricDao = ORMWorkoutMetricDAO()