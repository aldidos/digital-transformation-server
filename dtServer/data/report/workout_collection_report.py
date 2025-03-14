from dtServer.data.report.workout_report import WorkoutReport
from dtServer.data.report.base_report import BaseReport
import pandas as pd
from datetime import timedelta

class WorkoutColectionReport(BaseReport) : 

    def __init__(self) :         
        self.total_volume = 0 
        self.total_workout_time = timedelta()
        self.total_workouts = 0
        self.total_sets = 0
        self.avg_weight = 0 
        self.total_burned_kcl = 0 
        self.workout_reports = []

    def convert_data(self) : 
        self.total_volume = float(self.total_volume)
        self.total_workout_time = self.total_workout_time.total_seconds()
        self.total_workouts = int(self.total_workouts)
        self.total_sets = int(self.total_sets)
        self.avg_weight = float(self.avg_weight)
        self.total_burned_kcl = float(self.total_burned_kcl)

    def make_report(self, df : pd.DataFrame) : 
        self.total_volume = self.compute_volume(df)
        self.total_workouts = df['workout'].drop_duplicates().count()
        self.total_sets = df['set_id'].drop_duplicates().count()
        self.total_workout_time = self.compute_total_workout_time(df)

        groups = df.groupby('workout')
        for name, group in groups : 
            workout_id = name

            sub_df = pd.DataFrame(group)
            sub_df = sub_df.drop( columns = ['exercise_library_id', 'exercise_library', 'body_part_id', 'body_part']).drop_duplicates()
            workout_report = WorkoutReport(workout_id)
            workout_report.make_report(sub_df)

            self.workout_reports.append(workout_report) 

    def as_dict(self) : 
        self.convert_data()
        return {
            'total_volume' : self.total_volume,
            'total_workout_time' : self.total_workout_time,
            'total_workouts' : self.total_workouts,
            'total_sets' : self.total_sets,
            'avg_weight' : self.avg_weight, 
            'total_burned_kcl' : self.total_burned_kcl,
            'workout_reports' : [ d.as_dict() for d in self.workout_reports]
        }