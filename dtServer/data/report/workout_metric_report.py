import pandas as pd
import numpy as np
from dtServer.data.dto.workout_metric_report_dto import WorkoutMetricReportDTO
from dtServer.util.datetime_util import diff_time_second

class WorkoutMetricReport :     

    def make_report(self, df_workout_metriczs : pd.DataFrame) -> WorkoutMetricReportDTO : 
        df = df_workout_metriczs       

        means = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        max = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].max()
        
        head_df = df.head(3)
        tail_df = df.tail(3)
        first_values = head_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        last_values = tail_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()

        inc_values = last_values -  first_values
        inc_mean_velocity = inc_values['mean_velocity']

        sum_rep_duration = df_workout_metriczs['rep_duration'].sum()
        sum_rep_duration = float(sum_rep_duration)

        return WorkoutMetricReportDTO( means['mean_velocity'], means['mean_power'], max['mean_velocity'], max['mean_power'], 
                                    first_values['mean_velocity'], last_values['mean_velocity'], inc_mean_velocity, sum_rep_duration )
        
workoutMetricReport = WorkoutMetricReport()