import pandas as pd
from datetime import timedelta, time

def time_2_timedelta(t : time) : 
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)   

class BaseReport : 
       
    def sum_time_duration(self, time : pd.Series) : 
         timedeltas = time.transform(time_2_timedelta)
         return timedeltas.sum()

    def compute_volume(self, df : pd.DataFrame) : 
        df = df[['set_id', 'weight', 'total_reps']].drop_duplicates()
        volume = df['weight'] * df['total_reps']
        return volume.sum()