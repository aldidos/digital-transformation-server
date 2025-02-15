import pandas as pd
import numpy as np
from dtServer.data.dto.workout_metric_report_dto import WorkoutMetricReportDTO
from dtServer.util.datetime_util import diff_time_second

class WorkoutMetricReport :

    def __init__(self) : 
        self.mean_velocity = 0
        self.mean_power = 0
        self.max_velocity = 0
        self.max_power = 0
        self.first_mean_velocity = 0
        self.last_mean_velocity = 0
        self.inc_mean_velocity = 0
        self.sum_rep_duration = 0        

    def convert_datatype(self) : 
        self.mean_velocity = float(self.mean_velocity)
        self.mean_power = float(self.mean_power)
        self.max_velocity = float(self.max_velocity)
        self.max_power = float(self.max_power)
        self.first_mean_velocity = float(self.first_mean_velocity)
        self.last_mean_velocity = float(self.last_mean_velocity)
        self.inc_mean_velocity = float(self.inc_mean_velocity)
        self.sum_rep_duration = float(self.sum_rep_duration)      

    def make_report(self, df_workout_metrics : pd.DataFrame) -> WorkoutMetricReportDTO : 
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
        self.first_mean_velocity = first_values['mean_velocity']

        last_values = tail_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.last_mean_velocity = last_values['mean_velocity']

        inc_values = last_values -  first_values
        self.inc_mean_velocity = inc_values['mean_velocity']

        self.sum_rep_duration = df['rep_duration'].sum()
        self.sum_rep_duration = self.sum_rep_duration

        self.convert_datatype()
        return WorkoutMetricReportDTO( self.mean_velocity, self.mean_power, self.max_velocity, self.max_power, 
                                    self.first_mean_velocity, self.last_mean_velocity, self.inc_mean_velocity, self.sum_rep_duration )
        
workoutMetricReport = WorkoutMetricReport()