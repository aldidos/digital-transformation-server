import pandas as pd
from dtServer.data.report.base_report import BaseReport

class WorkoutSetReport(BaseReport) : 

    def __init__(self, set_id) : 
        self.set_id = set_id
        self.volume = 0 
        self.set = 0  ## Set order
        self.weight = 0
        self.total_reps = 0 
        self.total_rest_time = 0
        self.total_lifting_time = 0
        self.set_time_duration = 0

        self.mean_velocity = 0
        self.mean_power = 0
        self.max_velocity = 0
        self.max_power = 0
        self.initial_mean_velocity = 0
        self.last_mean_velocity = 0
        self.inc_mean_velocity = 0
        self.sum_rep_duration = 0

    def convert_datatype(self) : 
        self.volume = float(self.volume)
        self.set = int(self.set)
        self.weight = float(self.weight)
        self.total_reps = int(self.total_reps)

        self.mean_velocity = float(self.mean_velocity)
        self.mean_power = float(self.mean_power)
        self.max_velocity = float(self.max_velocity)
        self.max_power = float(self.max_power)
        self.initial_mean_velocity = float(self.initial_mean_velocity)
        self.last_mean_velocity = float(self.last_mean_velocity)
        self.inc_mean_velocity = float(self.inc_mean_velocity)
        self.total_lifting_time = float(self.sum_rep_duration)    

    def make_report(self, df : pd.DataFrame ) : 
        self.set = df['set'].iat[0]
        self.weight = df['weight'].iat[0]
        self.total_reps = df['total_reps'].iat[0]
        self.volume = self.compute_volume(df)
        set_end_time = df['set_end_time'].iat[0]
        set_start_time = df['set_start_time'].iat[0]
        self.set_time_duration = set_end_time - set_start_time

        means = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.mean_velocity = means['mean_velocity']
        self.mean_power =    means['mean_power']    

        max = df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].max()
        self.max_velocity = max['mean_velocity']
        self.max_power = max['mean_power']
        
        head_df = df.head(3)
        tail_df = df.tail(3)
        init_values = head_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.initial_mean_velocity = init_values['mean_velocity']

        last_values = tail_df[['mean_velocity', 'peak_velocity', 'mean_power', 'peak_power']].mean()
        self.last_mean_velocity = last_values['mean_velocity']

        inc_values = last_values -  init_values
        self.inc_mean_velocity = inc_values['mean_velocity']

        self.total_rep_duration = self.sum_time_duration(df['rep_duration'])
        self.total_rep_duration_con = self.sum_time_duration(df['rep_duration_con'])
        self.total_rep_duration_ecc = self.sum_time_duration(df['rep_duration_ecc'])
        self.total_top_stay_duration = self.sum_time_duration(df['top_stay_duration'])
        self.total_bottom_stay_duration = self.sum_time_duration(df['bottom_stay_duration'])

        self.convert_datatype() ####

    def as_dict(self) : 
        return {
            'set_id' : self.set_id,
            'set' : self.set, 
            'weight' : self.weight, 
            'total_reps' : self.total_reps, 
            'volume' : self.volume, 
            'set_time_duration' : self.set_time_duration,
            'mean_velocity' : self.mean_velocity, 
            'mean_power' : self.mean_power, 
            'max_velocity' : self.max_velocity, 
            'max_power' : self.max_power, 
            'initial_mean_velocity' : self.initial_mean_velocity, 
            'last_mean_velocity' : self.last_mean_velocity, 
            'inc_mean_velocity' : self.inc_mean_velocity, 
            'total_lifting_time' : self.total_lifting_time,
            'total_rep_duration' : self.total_rep_duration,
            'total_rep_duration_con' : self.total_rep_duration_con,
            'total_rep_duration_ecc' : self.total_rep_duration_ecc,
            'total_top_stay_duration' : self.total_top_stay_duration,
            'total_bottom_stay_duration' : self.total_bottom_stay_duration
        }