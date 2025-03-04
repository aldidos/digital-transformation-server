from dtServer.data.model.base_model import db_proxy, model_to_dict_or_none
from dtServer.data.dao.base_dao import BaseDAO, dict_to_model, model_to_dict
from dtServer.data.model.ormworkout.ormworkout import ORMWorkout
from dtServer.data.dao.ormworkout.ormworkout_exerciselib_dao import ormworkoutExerciseLibraryDao
from dtServer.data.dao.ormworkout.ormworkout_bodypart_dao import ormworkoutBodypartDao
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.model.user.user import User
from dtServer.data.model.equipment import Equipment

class ORMWorkoutDAO(BaseDAO) : 

    def save(self, user_id, equipment_id, date) : 
        data = {
            'user' : user_id, 
            'equipment' : equipment_id, 
            'date' : date
        }
        model = dict_to_model(ORMWorkout, data)
        return self.save_model( model )
    
    def insert(self, user_id, equipment_id, date) : 
        with db_proxy.atomic() : 
            ormworkout = self.save( user_id, equipment_id, date )
            ormworkout_id = ormworkout['id']

            exer_libs = exerciseLibraryDao.select_by_equipment(equipment_id)
            for exer_lib in exer_libs : 
                exercise_library_id = exer_lib['id']
                ormworkoutExerciseLibraryDao.save(ormworkout_id, exercise_library_id)

                body_parts = exerciseLibBodyPartDao.select_by_exercise_library_id(exercise_library_id)
                for body_part in body_parts : 
                    body_part_id = body_part['id']

                    ormworkoutBodypartDao.save( ormworkout_id, body_part_id )
            
            return ormworkout_id
    
    def select_by_user_date_period(self, user_id, from_date, to_date) : 
        q = ORMWorkout.select().where( ORMWorkout.user == user_id, ORMWorkout.date.between(from_date, to_date ))
        return [ model_to_dict(row) for row in q ]
    
    def get_by_id(self, id) : 
        model = ORMWorkout.get_by_id(id)
        return model_to_dict(model)
    
    def get_most_recent_by_equipment(self, user_id, equipment_id) : 
        q = ORMWorkout.select()\
            .join(User)\
            .join_from(ORMWorkout, Equipment)\
            .where(User.id == user_id, Equipment.id == equipment_id)\
            .order_by(ORMWorkout.date.desc())
        
        return model_to_dict_or_none( q.get_or_none() )    
    
    def get_recent_by_equipment(self, user_id, equipment_id) : 
        q = ORMWorkout.select()\
            .join(User)\
            .join_from(ORMWorkout, Equipment)\
            .where(User.id == user_id, Equipment.id == equipment_id)\
            .order_by(ORMWorkout.date.desc())\
            .limit(7)
        
        return [ row for row in q.dicts() ]  

ormWorkoutDao = ORMWorkoutDAO()