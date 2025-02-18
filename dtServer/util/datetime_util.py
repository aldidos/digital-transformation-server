import sys
sys.path.append('.')

from dtServer.data.model.base_model import DATETIME_FORMAT, TIME_FORMAT
from datetime import datetime, timedelta

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
        return 0
    diff_time = to_time - from_time 
    return diff_time.total_seconds()    

def second_to_minute(second) : 
    return second / 60

