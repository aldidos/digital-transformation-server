import pandas as pd

from dtServer.data.report.workout_session_report import workoutSessionReport
from dtServer.data.dto.workout_session_reports_dto import WorkoutSessionReportsDTO

class WokroutSessionReports : 

    def __init__(self):
        self.total_volume = 0 
        self.total_exercise_libraries = 0
        self.total_workout_time = 0
        self.list_workout_session_reports = []

    def make_report(self, list_dataset) : 

        for dataset in list_dataset : 
            workout_session = dataset['workout_session']
            workout_session_metric = dataset['workout_session_metric']

            ws_report = workoutSessionReport.make_report(workout_session_metric)

            self.total_volume = self.total_volume + ws_report.total_volume            

            self.list_workout_session_reports.append( {
                'date' : workout_session['date'], 
                'workout_session_report' : ws_report.as_dict()
                }
            )
        
        return WorkoutSessionReportsDTO(self.total_volume, self.total_exercise_libraries, self.total_workout_time, self.list_workout_session_reports)

workoutSessionReports = WokroutSessionReports()