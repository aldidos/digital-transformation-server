from peewee import *
from dtServer.data.model.base_model import BaseModel, DATETIME_FORMAT, db_proxy, model_to_dict_or_none
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.equipment import Equipment

class Workouts(BaseModel) : 
    workout_session = ForeignKeyField(WorkoutSessions)
    equipment = ForeignKeyField(Equipment)
    is_completed = BooleanField(null = False, default = False)
    completed_sets = IntegerField()    
    start_time = DateTimeField(DATETIME_FORMAT)
    end_time = DateTimeField(DATETIME_FORMAT)

    class Meta : 
        table_name = 'workouts'
        