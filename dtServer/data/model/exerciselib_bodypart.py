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

def insert_exerciselibrary_body_part(exercise_library, body_part) : 
    data = {
        'exercise_library' : exercise_library, 
        'body_part' : body_part
    }
    save_exercise_lib_body_part(data)

def select_bodyparts(exercise_library_id)  :
    q = ExerciseLibBodyPart.select(BodyPart).join(BodyPart).where(ExerciseLibBodyPart.exercise_library == exercise_library_id)
    return [row for row in q.dicts()]

def select_all_exercise_library_body_part() : 
    q = ExerciseLibBodyPart.select()
    list_data = [ model_to_dict(row) for row in q ]
    return list_data

def save_exercise_lib_body_part(data : dict) :
    model = dict_to_model(ExerciseLibBodyPart, data)    
    model.save()
    return model_to_dict(model)

def get_exercise_lib_body_part(exercise_library_id : int, body_part_id : int) : 
    model = ExerciseLibBodyPart.select().where(ExerciseLibBodyPart.exercise_library == exercise_library_id and ExerciseLibBodyPart.body_part == body_part_id).get()
    return model_to_dict_or_none(model)

def get_exercise_lib_body_part_by_library(exercise_library_id : int) : 
    q = ExerciseLibBodyPart.select().where( ExerciseLibBodyPart.exercise_library == exercise_library_id )
    list_data = [model_to_dict(row) for row in q]
    return list_data

def get_exercise_lib_body_part_by_body_part(body_part_id : int) : 
    q = ExerciseLibBodyPart.select().where( ExerciseLibBodyPart.body_part == body_part_id )
    list_data = [model_to_dict(row) for row in q]
    return list_data
