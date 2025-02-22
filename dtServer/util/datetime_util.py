import sys
sys.path.append('.')

from dtServer.data.model.base_model import DATETIME_FORMAT, TIME_FORMAT
from datetime import datetime, timedelta, time

def diff_time_second(from_datetime_time, to_datetime_time) : 
    str_start_time = from_datetime_time.isoformat()
    str_end_time = to_datetime_time.isoformat()

    start_time = datetime.strptime(str_start_time, TIME_FORMAT)
    end_time = datetime.strptime(str_end_time, TIME_FORMAT)

    total_second = compute_diff_to_seconds(start_time, end_time)

    return total_second

def diff_datetime(from_datetime, to_datetime) : 
    str_start_time = from_datetime.isoformat()
    str_end_time = to_datetime.isoformat()

    start_time = datetime.strptime(str_start_time, DATETIME_FORMAT)
    end_time = datetime.strptime(str_end_time, DATETIME_FORMAT)

    total_second = compute_diff_to_seconds(start_time, end_time)

    return total_second

def compute_diff_to_seconds(from_time, to_time) : 
    if not isinstance(from_time, datetime) or not isinstance(to_time, datetime) : 
        return timedelta()
    diff_time = to_time - from_time 
    return diff_time 

def second_to_minute(second) : 
    return second / 60

def timedelta_to_dhm_format(td : timedelta) : 
    seconds = td.total_seconds() % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    day = td.days

    return {
        'day' : day, 
        'hour' : hour, 
        'minutes' : minutes, 
        'seconds' : seconds
    }   
    