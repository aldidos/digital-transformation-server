from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import datetime

def model_to_dict_or_none(model) : 
    if model == None : 
        return None
    return model_to_dict(model)

def str_to_date(date_str : str) : 
    f = '%Y-%m-%d'
    return datetime.strptime(date_str, f).date()

def str_to_datetime(date_str : str) : 
    f = '%Y-%m-%d %H:%M%S'
    return datetime.strptime(date_str, f)