from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.user import User
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.body_part import BodyPart
from dtServer.data.model.workout_metrics import WorkoutMetrics

class WorkoutData(BaseModel) :
    user = ForeignKeyField(User) 
    workout_session = ForeignKeyField(WorkoutSessions)
    exercise_library = ForeignKeyField(ExerciseLibrary) 
    body_part = ForeignKeyField(BodyPart) 
    workout_metric = ForeignKeyField(WorkoutMetrics)
    
    class Meta : 
        table_name = 'workout_data'