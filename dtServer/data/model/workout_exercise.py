from peewee import *
from dtServer.data.model.base_model import BaseModel, db_proxy
from dtServer.data.model.exercise_library import ExerciseLibrary

from dtServer.data.model.workouts import WorkoutSessions
from dtServer.data.model.user import User
from dtServer.data.model.workout_metrics import WorkoutMetrics
from playhouse.shortcuts import model_to_dict, dict_to_model

class WorkoutExercise(BaseModel) :
    user = ForeignKeyField(User)
    workout_session = ForeignKeyField(WorkoutSessions)
    exercise_library = ForeignKeyField(ExerciseLibrary)
    workout_metric = ForeignKeyField(WorkoutMetrics)

    class Meta : 
        table_name = 'workout_exercise'