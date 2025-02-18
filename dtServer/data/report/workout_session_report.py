import pandas as pd
from dtServer.data.report.base_report import BaseReport
from dtServer.data.report.workout_report import WorkoutReport

class WokroutSessionReport(BaseReport) : 

    def __init__(self, workout_session_id):
        self.workout_session_id = workout_session_id
        self.total_volume = 0
        self.total_sets = 0
        self.total_workouts = 0
        self.total_workout_time = 0
        self.total_burned_kcl = 0 ####  

        self.exercise_libraries = []
        self.body_parts = []

        self.wokrout_reports = []

    def convert_datatype(self) : 
        self.total_volume = float(self.total_volume)
        self.total_sets = int(self.total_sets)
        self.total_workouts = int(self.total_workouts)

    def compute_body_part_info(self, df : pd.DataFrame) : ####
        groups = df.groupby(['body_part_id', 'body_part'])
        list = []
        for name, group in groups : 
            body_part_id = name[0]
            body_part_name = name[1]
            
            volume = self.compute_volume(group) 
            usage_freq = group[['set_id']].drop_duplicates().count()
            usage_freq = usage_freq / self.total_sets

            list.append({ 
                'body_part_id' : body_part_id, 
                'name' : body_part_name,
                'volume' : float(volume), 
                'usage_freq' : float(usage_freq)
            })

        return list

    def compute_exercise_lib_info(self, df : pd.DataFrame) : ####

        groups = df.groupby(['exercise_library_id', 'exercise_library'])
        list = []
        for name, group in groups : 
            exer_lib_id = name[0]
            exer_name = name[1]
            
            volume = self.compute_volume(group)

            usage_freq = group[['set_id']].drop_duplicates().count()
            usage_freq = usage_freq / self.total_sets

            list.append({ 
                'exercise_library_id' : exer_lib_id, 
                'name' : exer_name,
                'volume' : float(volume), 
                'usage_freq' : float(usage_freq)
            })

        return list

    def make_report(self, df : pd.DataFrame) : 
        self.total_sets = df['set_id'].drop_duplicates().count()
        self.total_workouts = df['workout'].drop_duplicates().count()

        self.exercise_libraries = self.compute_exercise_lib_info(df)        
        self.body_parts = self.compute_body_part_info(df)

        groups = df.groupby('workout')
        for name, workout_dataset in groups :            
            workout_id = name

            workout_dataset = workout_dataset.drop( columns = ['exercise_library_id', 'exercise_library', 'body_part_id', 'body_part']).drop_duplicates()

            workout_report = WorkoutReport(workout_id)
            workout_report.make_report(workout_dataset) 

            self.wokrout_reports.append(workout_report) 
        
        self.total_volume = self.compute_volume( df )

        self.convert_datatype()

    def as_dict(self) : 
        return {
            'workout_session_id' : self.workout_session_id,
            'total_volume' : self.total_volume,
            'total_sets' : self.total_sets,
            'total_workout_time' : self.total_workout_time,
            'total_workouts' : self.total_workouts,
            'exercise_libraries' : [ d for d in self.exercise_libraries ],
            'body_parts' : [ d for d in self.body_parts ],
            'workout_reports' : [d.as_dict() for d in self.wokrout_reports]
        }