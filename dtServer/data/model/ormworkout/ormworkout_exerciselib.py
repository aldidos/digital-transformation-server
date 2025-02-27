from peewee import *
from dtServer.data.model.base_model import BaseModel
from dtServer.data.model.ormworkout.ormworkout import ORMWorkout
from dtServer.data.model.exercise_library import ExerciseLibrary

class ORMWorkoutExerciseLibrary(BaseModel) : 
    ormworkout = ForeignKeyField(ORMWorkout)    
    exercise_library = ForeignKeyField(ExerciseLibrary)    

    class Meta : 
        table_name = 'ormworkout_exerciselibrary'