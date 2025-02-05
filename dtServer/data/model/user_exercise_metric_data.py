from peewee import *
from dtServer.data.model.base_model import BaseModel, model_to_dict_or_none, db_proxy
from dtServer.data.model.user_exercise_metric import UserExerciseMetric
from dtServer.data.model.user_exercise_metric_value import UserExerciseMetricValue, save_user_exercise_metric_value

class UserExerciseMetricData(BaseModel) : 
    user_exercise_metric = ForeignKeyField(UserExerciseMetric)
    user_exercise_metric_value = ForeignKeyField(UserExerciseMetricValue)

    class Meta : 
        table_name = 'user_exercise_metric_data'

def insert_many_user_exercise_metric_data(data) : 
    user_exercise_metric = data['user_exercise_metric_id']
    list_user_exercise_metric_value = data['user_exercise_metric_values']

    with db_proxy.atomic() : 
        list_data = [] 
        for user_exercise_metric_value in list_user_exercise_metric_value : 
            temp_uemv = save_user_exercise_metric_value(user_exercise_metric_value)
            list_data.append( {
                'user_exercise_metric' : user_exercise_metric,
                'user_exercise_metric_value' : temp_uemv['id']
                } )
        UserExerciseMetricValue.insert_many(list_data).execute()
