from datetime import datetime, timedelta

def diff_time_second(from_datetime_time, to_datetime_time) : 
    str_start_time = from_datetime_time.isoformat()
    str_end_time = to_datetime_time.isoformat()

    start_time = datetime.strptime(str_start_time, '%H:%M:%S')
    end_time = datetime.strptime(str_end_time, '%H:%M:%S')

    diff = end_time - start_time 
    total_second = diff.total_seconds()

    return total_second

