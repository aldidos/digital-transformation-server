import pandas as pd
from datetime import timedelta, time
from dtServer.util.datetime_util import compute_diff_to_seconds

def time_2_timedelta(t : time) : 
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)   

class BaseReport : 
       
    def sum_time_duration(self, time : pd.Series) : 
         timedeltas = time.transform(time_2_timedelta)
         return timedeltas.sum()
    
    def compute_total_lifting_time(self, df : pd.DataFrame) :
        df = df[['set_id', 'rep', 'rep_duration']].drop_duplicates()
        self.sum_time_duration(df['rep_duration'])

    def compute_volume(self, df : pd.DataFrame) : 
        df = df[['set_id', 'weight', 'total_reps']].drop_duplicates()
        volume = df['weight'] * df['total_reps']
        return volume.sum()
    
    def compute_total_reps(self, df : pd.DataFrame) : 
        total_reps = df[['set_id', 'total_reps']].drop_duplicates()['total_reps'].sum()
        return total_reps
    
    def compute_total_workout_time(self, df : pd.DataFrame) : 
        df = df[['workout', 'workout_end_time', 'workout_start_time']].drop_duplicates()
        workout_time_duration = df['workout_end_time'] - df['workout_start_time']
        workout_time_duration = workout_time_duration.sum()
        return workout_time_duration
    
    def compute_set_time_duration(self, df : pd.DataFrame) : 
        df = df[['set_id', 'set_start_time', 'set_end_time']].drop_duplicates()
        return self.compute_time_duration(df)

    def compute_res_time_duration(self, df : pd.DataFrame) : 
        df = df[['set_id', 'res_start_time', 'res_end_time']].drop_duplicates()
        return self.compute_time_duration(df)

    def compute_time_duration(self, df : pd.DataFrame) : 
        total_time_duration = timedelta()
        for v in df.values : 
            from_time = v[1]
            to_time = v[2]         
            total_time_duration = total_time_duration + compute_diff_to_seconds(from_time, to_time)        
        return total_time_duration