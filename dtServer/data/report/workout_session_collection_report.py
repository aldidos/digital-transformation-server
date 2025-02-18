import pandas as pd
from dtServer.data.report.workout_session_report import WokroutSessionReport
from dtServer.data.report.base_report import BaseReport

class WokroutSessionCollectionReport(BaseReport) : 

    def __init__(self):        
        self.total_volume = 0 
        self.total_workout_time = 0
        self.total_workouts = 0
        self.total_sets = 0
        self.workout_session_reports = []

    def conver_datatype(self) : 
        self.total_sets = int(self.total_sets)
        self.total_volume = float(self.total_volume)
        self.avg_reps_pet_set = float(self.avg_reps_pet_set)
        self.total_workout_time = float(self.total_workout_time)

    def make_report(self, df : pd.DataFrame) : 
        self.from_date = df['date'].min()
        self.to_date = df['date'].max()        
        self.total_volume = self.compute_volume(df)
        self.total_workouts = df['workout'].drop_duplicates().count()
        self.total_sets = df['set_id'].drop_duplicates().count()

        groups = df.groupby('workout_session')

        for name, group in groups : 
            workout_session_id = name       

            ws_report = WokroutSessionReport(workout_session_id) 
            ws_report.make_report(group)

            self.workout_session_reports.append(ws_report)        
        
    def as_dict(self) :

        return {
            'from' : self.from_date, 
            'to' : self.to_date, 
            'total_volume' : self.total_volume, 
            'total_workout_time' : self.total_workout_time, 
            'total_sets' : self.total_sets, 
            'total_workouts' : self.total_workouts,
            'workout_session_reports' : [d.as_dict() for d in self.workout_session_reports]
        }           
