import pandas as pd
from dtServer.data.report.base_report import BaseReport
from dtServer.data.report.workout_report import WorkoutReport
from datetime import timedelta

class WokroutSessionReport(BaseReport) : 

    def __init__(self, workout_session_id):
        self.workout_session_id = workout_session_id        
        self.total_volume = 0
        self.total_sets = 0
        self.total_workouts = 0
        self.total_workout_time = timedelta()
        self.total_burned_kcl = 0 ####  

        self.exercise_library_reports = []
        self.body_part_reports = []

        self.wokrout_reports = []

    def attrs() : 
        attrs = ['exercise_library_id', 'exercise_library', 'body_part_id', 'body_part'  ]
        attrs.extend(WorkoutReport.attrs())
        return attrs

    def convert_datatype(self) : 
        self.total_volume = float(self.total_volume)
        self.total_sets = int(self.total_sets)
        self.total_workouts = int(self.total_workouts)
        self.total_workout_time = self.total_workout_time.total_seconds()

    def compute_part_reports(self, part_id, part_name, df : pd.DataFrame) : ####
        groups = df.groupby([part_id, part_name])
        list_reports = []
        for part_name, group in groups : 
            part_id = part_name[0]
            part_name = part_name[1]
            
            volume = self.compute_volume(group) 
            usage_freq = group['set_id'].drop_duplicates().count()
            usage_freq = usage_freq / self.total_sets

            list_reports.append({ 
                'id' : int(part_id), 
                'name' : part_name,
                'volume' : float(volume), 
                'usage_freq' : float(usage_freq)
            })

        return list_reports

    def make_report(self, df : pd.DataFrame) : 
        attrs = WokroutSessionReport.attrs()
        df = df[ attrs ].drop_duplicates()

        self.date = df['date'].iat[0].isoformat()
        self.total_sets = df['set_id'].drop_duplicates().count()
        self.total_workouts = df['workout'].drop_duplicates().count()

        self.exercise_library_reports = self.compute_part_reports('exercise_library_id', 'exercise_library', df) 
        self.body_part_reports = self.compute_part_reports('body_part_id', 'body_part', df) 
        self.total_volume = self.compute_volume( df )

        self.total_workout_time = self.compute_total_workout_time(df)

        groups = df.groupby('workout')
        for name, workout_dataset in groups :            
            workout_id = name            

            workout_report = WorkoutReport(workout_id)
            workout_report.make_report(workout_dataset)            

            self.wokrout_reports.append(workout_report)                 

    def as_dict(self) : 
        self.convert_datatype()
        return {
            'workout_session_id' : self.workout_session_id,
            'date' : self.date, 
            'total_volume' : self.total_volume,
            'total_sets' : self.total_sets,
            'total_workout_time' : self.total_workout_time,
            'total_workouts' : self.total_workouts,
            'exercise_library_reports' : [ d for d in self.exercise_library_reports ],
            'body_part_reports' : [ d for d in self.body_part_reports ],
            'workout_reports' : [d.as_dict() for d in self.wokrout_reports]
        }