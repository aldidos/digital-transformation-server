import pandas as pd
import numpy as np
from dtServer.util.datetime_util import diff_time_second
from datetime import timedelta

def time_2_timedelta(t) : 
    return timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)    

class WorkoutMetricReport :

    def __init__(self) : 
        self.mean_velocity = 0
        self.mean_power = 0
        self.max_velocity = 0
        self.max_power = 0
        self.initial_mean_velocity = 0
        self.last_mean_velocity = 0
        self.inc_mean_velocity = 0
        
        self.total_rep_duration = 0
        self.total_rep_duration_con = 0
        self.total_rep_duration_ecc = 0
        self.total_top_stay_duration = 0
        self.total_bottom_stay_duration = 0

    def convert_datatype(self) : 
        self.mean_velocity = float(self.mean_velocity)
        self.mean_power = float(self.mean_power)
        self.max_velocity = float(self.max_velocity)
        self.max_power = float(self.max_power)
        self.initial_mean_velocity = float(self.initial_mean_velocity)
        self.last_mean_velocity = float(self.last_mean_velocity)
        self.inc_mean_velocity = float(self.inc_mean_velocity)
        self.total_rep_duration = self.total_rep_duration.total_seconds()
        self.total_rep_duration_con = self.total_rep_duration_con.total_seconds()
        self.total_rep_duration_ecc = self.total_rep_duration_ecc.total_seconds()
        self.total_top_stay_duration = self.total_top_stay_duration.total_seconds()
        self.total_bottom_stay_duration = self.total_bottom_stay_duration.total_seconds()

    def total_time_duration(self, time) : 
         timedeltas = time.transform(time_2_timedelta)
         return timedeltas.sum()

    def make_report(self, df_workout_metrics : pd.DataFrame) : 
        df = df_workout_metrics       

        means = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.mean_velocity = means['mean_velocity']
        self.mean_power =    means['mean_power']    

        max = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].max()
        self.max_velocity = max['mean_velocity']
        self.max_power = max['mean_power']
        
        head_df = df.head(3)
        tail_df = df.tail(3)
        first_values = head_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.initial_mean_velocity = first_values['mean_velocity']

        last_values = tail_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.last_mean_velocity = last_values['mean_velocity']

        inc_values = last_values -  first_values
        self.inc_mean_velocity = inc_values['mean_velocity']

        self.total_rep_duration = self.total_time_duration(df['rep_duration'])
        self.total_rep_duration_con = self.total_time_duration(df['rep_duration_con'])
        self.total_rep_duration_ecc = self.total_time_duration(df['rep_duration_ecc'])
        self.total_top_stay_duration = self.total_time_duration(df['top_stay_duration'])
        self.total_bottom_stay_duration = self.total_time_duration(df['bottom_stay_duration'])

        self.convert_datatype() ####
                
    def as_dict(self) : 
        return {
            'mean_velocity' : self.mean_velocity, 
            'mean_power' : self.mean_power,
            'max_velocity' : self.max_velocity, 
            'max_power' : self.max_power,
            'initial_mean_velocity' : self.initial_mean_velocity,
            'inc_mean_velocity' : self.inc_mean_velocity,
            'last_mean_velocity' : self.last_mean_velocity, 
            'total_rep_duration' : self.total_rep_duration,
            'total_rep_duration_con' : self.total_rep_duration_con,
            'total_rep_duration_ecc' : self.total_rep_duration_ecc,
            'total_top_stay_duration' : self.total_top_stay_duration,
            'total_bottom_stay_duration' : self.total_bottom_stay_duration
        }