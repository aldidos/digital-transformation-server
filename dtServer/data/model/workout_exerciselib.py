from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.workout.workouts import Workouts
from dtServer.data.model.exercise_library import ExerciseLibrary

class WorkoutExerciseLib(BaseModel) : 
    workout = ForeignKeyField(Workouts)   
    exercise_library = ForeignKeyField(ExerciseLibrary)

    class Meta  :
        table_name = 'workout_exerciselib'