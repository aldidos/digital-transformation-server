import pandas as pd

from dtServer.data.report.workout_session_report import WokroutSessionReport

class WokroutSessionCollectionReport : 

    def __init__(self):
        self.total_volume = 0 
        self.total_workout_time = 0
        self.total_workouts = 0
        self.total_sets = 0
        self.list_workout_session_reports = []

    def make_report(self, list_dataset) : 

        for dataset in list_dataset : 
            workout_session = dataset['workout_session']
            workout_session_metric = dataset['workout_session_metric']

            ws_report = WokroutSessionReport()
            ws_report.make_report(workout_session_metric)

            self.total_volume = self.total_volume + ws_report.total_volume
            self.total_workout_time = self.total_workout_time + ws_report.total_workout_time
            self.total_sets = self.total_sets + ws_report.total_sets
            self.total_workouts = self.total_workouts + ws_report.total_workouts

            self.list_workout_session_reports.append( {
                'date' : workout_session['date'], 
                'workout_session_report' : ws_report.as_dict()
                }
            )
        
    def as_dict(self) :

        return {
            'total_volume' : self.total_volume, 
            'total_workout_time' : self.total_workout_time, 
            'total_sets' : self.total_sets, 
            'total_workouts' : self.total_workouts,
            'list_workout_session_reports' : [d for d in self.list_workout_session_reports]
        }           
