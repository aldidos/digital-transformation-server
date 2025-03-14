from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none
from dtServer.data.model.exercise_library import ExerciseLibrary
from dtServer.data.model.body_part import BodyPart
from playhouse.shortcuts import model_to_dict, dict_to_model

class ExerciseLibBodyPart(BaseModel) : 
    exercise_library = ForeignKeyField(ExerciseLibrary, backref='exercise_library')
    body_part = ForeignKeyField(BodyPart, backref='body_part')

    class Meta : 
        table_name = 'exerciselib_bodypart'

