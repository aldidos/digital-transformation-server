from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workouts import Workouts, db_proxy, model_to_dict_or_none
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.workout_exerciselib import WorkoutExerciseLib
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao
from dtServer.data.dao.workout_exerciselib_dao import workoutExerciselibDao
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.dao.workout_bodypart_dao import workoutBodypartDao
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutsDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(Workouts, data) )
    
    def select_by_id(self, id : int) : 
        workout =  Workouts.get_or_none(Workouts.id == id)    
        return model_to_dict_or_none(workout)

    def select_by_workout_session(self, workout_session_id : int) : 
        q = Workouts.select().where( Workouts.workout_session == workout_session_id )
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def select_by_user_and_date_period(self, user_id, from_date, to_date) : 
        q = Workouts.select( Equipment.id.alias('equipment'), Workouts.completed_sets, Workouts.start_time, Workouts.end_time)\
            .join(WorkoutSessions)\
            .join(User)\
            .join_from(Workouts, Equipment)\
            .where(WorkoutSessions.is_completed == True, User.id == user_id,  WorkoutSessions.date.between(from_date, to_date))
        
        return [ row for row in q.dicts() ]
    
    def select_recent_user_exercise_library_workouts(self, user_id, exercise_library_id) : 
        q = Workouts.select( WorkoutSessions.id.alias('workout_session'), WorkoutSessions.date, 
                            Workouts.id.alias('workout'), Workouts.completed_sets, Workouts.start_time, Workouts.end_time,
                            )\
                            .join(WorkoutSessions)\
                            .join(User)\
                            .join_from(Workouts, WorkoutExerciseLib)\
                            .join(ExerciseLibrary)\
                            .where(Workouts.is_completed == True, User.id == user_id, ExerciseLibrary.id == exercise_library_id)\
                            .order_by(WorkoutSessions.date.desc())\
                            .limit(7)
        
        return [ row for row in q.dicts() ]
    
    def insert(self, data) : 
        with db_proxy.atomic() : 
            workout_id = Workouts.insert(data).execute()
            equipment_id = data['equipment']
            list_exercise_lib = exerciseLibraryDao.select_by_equipment(equipment_id)
            for exer_lib in list_exercise_lib : 
                exer_lib_id = exer_lib['id'] 
                workoutExerciselibDao.create(workout_id, exer_lib_id)

                list_body_parts = exerciseLibBodyPartDao.select_by_exercise_library_id(exer_lib_id)
                for body_part in list_body_parts : 
                    body_part_id = body_part['id']
                    workoutBodypartDao.create(workout_id, body_part_id)
                    
            return workout_id

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            Workouts.insert_many(list_data).execute()
    
workoutDao = WorkoutsDao()