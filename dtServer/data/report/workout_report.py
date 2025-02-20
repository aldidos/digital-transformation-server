import pandas as pd
from dtServer.data.report.workout_set_report import WorkoutSetReport
from dtServer.data.report.base_report import BaseReport

class WorkoutReport(BaseReport) :      

    def attrs() :         
        attrs = ['date', 'workout', 'completed_sets', 'workout_start_time', 'workout_end_time'] 
        attrs.extend( WorkoutSetReport.attrs() )
        return attrs 

    def __init__(self, workout_id) : 
        self.workout_id = workout_id
        self.total_sets = 0
        self.total_volume = 0
        self.total_reps = 0
        self.total_lifting_time = 0
        self.avg_weight = 0
        self.avg_reps_pet_set = 0
        self.total_workout_time = 0 
        self.total_burned_kcl = 0 #### 소모 칼로리
        self.intensity = 0  #### 운동 강도

        self.workout_set_reports = []

    def conver_datatype(self) : 
        self.total_sets = int(self.total_sets)
        self.total_volume = float(self.total_volume)
        self.total_reps = int(self.total_reps)        
        self.avg_weight = float(self.avg_weight)
        self.avg_reps_pet_set = float(self.avg_reps_pet_set)
    
    def compute_total_workout_time(self, df : pd.DataFrame) : 
        df = df[['workout', 'workout_end_time', 'workout_start_time']]
        workout_time_duration = df['workout_end_time'] - df['workout_start_time']
        workout_time_duration = workout_time_duration.sum()
        return workout_time_duration.total_seconds()

    def make_report(self, df : pd.DataFrame ) : 
        workout_attrs = WorkoutReport.attrs()
        df = df[ workout_attrs ].drop_duplicates()

        self.date = df['date'].iat[0].isoformat()
        self.total_sets = df['completed_sets'].iat[0]
        self.total_reps = df[['set_id', 'total_reps']].drop_duplicates()['total_reps'].sum()
        self.total_volume = self.compute_volume( df )
        sum_weight = df[['set_id', 'weight']].drop_duplicates()['weight'].sum()        
        self.avg_weight = sum_weight / self.total_sets
        self.avg_reps_pet_set = self.total_reps / self.total_sets        
        self.total_workout_time = self.compute_total_workout_time( df )
        
        set_groups = df.groupby([ 'set_id' ])
        for name, set_dataset in set_groups : 
            set_id = name[0]
            workout_set_report = WorkoutSetReport(set_id)
            workout_set_report.make_report(set_dataset)

            self.total_lifting_time = self.total_lifting_time + workout_set_report.total_rep_duration
            self.total_burned_kcl = self.total_burned_kcl + workout_set_report.burned_kcl

            self.workout_set_reports.append( workout_set_report )
        
        self.conver_datatype()        
             
    def as_dict(self) : 
        return {
            'wokrout_id' : self.workout_id,
            'date' : self.date,
            'total_workout_time' : self.total_workout_time, 
            'total_lifting_time' : self.total_lifting_time, 
            'total_sets' : self.total_sets, 
            'total_volume' : self.total_volume, 
            'total_reps' : self.total_reps, 
            'avg_reps_pet_set' : self.avg_reps_pet_set, 
            'avg_weight' : self.avg_weight,
            'burned_kcl' : self.total_burned_kcl,
            'intensity' : self.intensity,            
            'set_reports' : [ d.as_dict() for d in self.workout_set_reports]
        }
