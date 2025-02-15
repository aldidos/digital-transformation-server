import pandas as pd

from dtServer.data.report.workout_report import workoutReport
from dtServer.data.dto.workout_session_report_dto import WorkoutSessionReportDTO

class WokroutSessionReport : 

    def __init__(self):
        self.total_volume = 0
        self.total_sets = 0
        self.total_exercise_libraries = 0
        self.total_workout_time = 0
        self.total_workouts = 0
        self.list_workout_reports = []

    def convert_datatype(self) : 
        self.total_volume = float(self.total_volume)
        self.total_sets = int(self.total_sets)
        self.total_exercise_libraries = int(self.total_exercise_libraries)
        self.total_workout_time = self.total_workout_time.total_seconds()
        self.total_workouts = int(self.total_workouts)

    def compute_total_workout_time(self, df : pd.DataFrame) : 
        sub_df = df[['workout', 'start_time', 'end_time']].drop_duplicates()
        df['diff_time'] = df['end_time'] - df['start_time']
        self.total_workout_time = df['diff_time'].sum()

    def make_report(self, workout_session_metrics) : 
        df = pd.DataFrame(workout_session_metrics)

        self.total_exercise_libraries = df['exercise_library'].drop_duplicates().count()
        self.totla_workout_time = self.compute_total_workout_time(df)
        self.total_workouts = df['workout'].drop_duplicates().count()

        groups = df.groupby(['workout', 'completed_sets', 'start_time', 'end_time', 'exercise_library'])

        for name, dataset in groups : 
            workout = {
                'workout' : name[0], 
                'completed_sets' : name[1], 
                'start_time' : name[2], 
                'end_time' : name[3], 
                'exercise_library' : name[4]
            }

            workout_report = workoutReport.make_report(workout, dataset) 
            self.total_sets = self.total_sets + workout_report.total_sets
            self.total_volume = self.total_volume + workout_report.total_volume

            self.list_workout_reports.append( workout_report.as_dict() ) 

        self.convert_datatype()
        return WorkoutSessionReportDTO(self.total_volume, self.total_sets, self.total_exercise_libraries, self.total_workout_time, self.total_workouts, self.list_workout_reports)

workoutSessionReport = WokroutSessionReport()