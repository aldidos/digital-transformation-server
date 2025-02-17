from dtServer.data.model.base_model import DATETIME_FORMAT, TIME_FORMAT
from datetime import datetime, timedelta

def diff_time_second(from_datetime_time, to_datetime_time) : 
    str_start_time = from_datetime_time.isoformat()
    str_end_time = to_datetime_time.isoformat()

    start_time = datetime.strptime(str_start_time, TIME_FORMAT)
    end_time = datetime.strptime(str_end_time, TIME_FORMAT)

    diff = end_time - start_time 
    total_second = diff.total_seconds()

    return total_second

def diff_datetime(from_datetime, to_datetime) : 
    str_start_time = from_datetime.isoformat()
    str_end_time = to_datetime.isoformat()

    start_time = datetime.strptime(str_start_time, DATETIME_FORMAT)
    end_time = datetime.strptime(str_end_time, DATETIME_FORMAT)

    diff = end_time - start_time 
    total_second = diff.total_seconds()

    return total_second

def second_to_minute(second) : 
    return second / 60