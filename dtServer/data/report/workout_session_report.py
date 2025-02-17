import pandas as pd

from dtServer.data.report.workout_report import WorkoutReport
from dtServer.data.dto.workout_session_report_dto import WorkoutSessionReportDTO

class WokroutSessionReport : 

    def __init__(self):
        self.total_volume = 0
        self.total_sets = 0
        self.total_workouts = 0
        self.total_workout_time = 0
        self.total_burned_kcl = 0 ####

        self.exercise_libs_workout_set_freq = {}
        self.body_part_workout_set_freq = {}

        self.list_workout_reports = []

    def convert_datatype(self) : 
        self.total_volume = float(self.total_volume)
        self.total_sets = int(self.total_sets)
        self.total_workouts = int(self.total_workouts)

    def add_workout_set_freq(self, workout_set_dict : dict, key, val) : 
        v = workout_set_dict.get(key)
        if not v : 
            v = 0
        v = v + val
        workout_set_dict[key] = v        
   
    def make_report(self, workout_session_metrics) : 
        df = pd.DataFrame(workout_session_metrics)

        self.total_workouts = df['workout'].drop_duplicates().count()

        groups = df.groupby(['workout', 'completed_sets', 'start_time', 'end_time'])

        for name, dataset in groups : 
            workout = {
                'workout' : name[0], 
                'completed_sets' : name[1], 
                'start_time' : name[2], 
                'end_time' : name[3]
            }

            workout_report = WorkoutReport().make_report(workout, dataset) 
            self.total_sets = self.total_sets + workout_report.total_sets
            self.total_volume = self.total_volume + workout_report.total_volume
            self.total_workout_time = self.total_workout_time + workout_report.total_workout_time

            for exercise_lib in workout_report.exercise_libraries : 
                self.add_workout_set_freq(self.exercise_libs_workout_set_freq, exercise_lib, workout_report.total_sets )

            for body_part in workout_report.body_parts : 
                self.add_workout_set_freq(self.body_part_workout_set_freq, body_part, workout_report.total_sets )

            self.list_workout_reports.append( workout_report ) 

        self.convert_datatype()
        return WorkoutSessionReportDTO(self.total_volume, self.total_sets, self.total_workout_time, self.total_workouts, self.exercise_libs_workout_set_freq, self.body_part_workout_set_freq, self.list_workout_reports)
