from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_metrics import WorkoutMetrics, db_proxy
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.user import User
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutMetricsDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutMetrics, data) )
    
    def insert_many(self, list_data) : 
        with db_proxy.atomic() : 
            list_ids = []
            for data in list_data : 
                id = WorkoutMetrics.insert(data).execute()
                list_ids.append(id)
            return list_ids    

    def select(self, user_id, from_date, to_date) : 
        q = WorkoutMetrics.select(Workouts.workout_session.date.alias('date'), ExerciseLibrary.name.alias('exercise_library_name'), WorkoutMetrics.set, WorkoutMetrics.rep\
                        , WorkoutMetrics.weight, WorkoutMetrics.volume, WorkoutMetrics.peak_velocity, WorkoutMetrics.mean_velocity, WorkoutMetrics.peak_power, WorkoutMetrics.mean_power, WorkoutMetrics.height, WorkoutMetrics.power )\
            .join(Workouts)\
            .join(WorkoutSessions)\
            .join(User)\
            .join_from(Workouts, ExerciseLibrary)\
            .where(User.id == user_id, WorkoutSessions.date.between(from_date, to_date) )
        
        list_data = [ row for row in q.dicts() ]
        return list_data
    
workoutMetricDao = WorkoutMetricsDao()
