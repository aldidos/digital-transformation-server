from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.workout_sessions import WorkoutSessions, db_proxy
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutSessionsDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(WorkoutSessions, data) )
    
    def insert(self, user_id, date, status) : 
        data = {
            'user' : user_id, 
            'date' : date, 
            'status' : status, 
            'is_completed' : False
        }
        return self.save(date)

    def select_by_id(self, id) : 
        model = WorkoutSessions.select().where(WorkoutSessions.id == id).get()
        return model_to_dict(model)

    def select_by_user_and_date(self, user_id, date ) : 
        q = WorkoutSessions.select().where( WorkoutSessions.user == user_id and WorkoutSessions.date == date )
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def select_by_user_and_date_period(self, user_id, from_date, to_date ) : 
        q = WorkoutSessions.select().where( WorkoutSessions.user == user_id and WorkoutSessions.date.between(from_date, to_date) )
        list_data = [model_to_dict(row) for row in q]
        return list_data

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            WorkoutSessions.insert_many(list_data).execute()

workoutSessionDao = WorkoutSessionsDao()