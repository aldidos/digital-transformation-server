import pandas as pd
from dtServer.data.report.workout_metric_report import workoutMetricReport
from dtServer.data.dto.workout_set_report_dto import WorkoutSetReportDTO

class WorkoutSetReport : 

    def __init__(self) : 
        self.volume = 0 
        self.set = 0
        self.weight = 0
        self.total_reps = 0 
        self.total_rest_time = 0
        self.total_lifting_time = 0

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

    def make_report(self, set_info, workout_metrics : dict ) : 
        df = pd.DataFrame(workout_metrics)
        self.set = set_info['set']
        self.weight = set_info['weight']
        self.total_reps = set_info['total_reps']
        self.volume = self.weight * self.total_reps        

        wm_report = workoutMetricReport.make_report(df)
        self.mean_velocity = wm_report.mean_velocity
        self.mean_power = wm_report.mean_power
        self.max_velocity = wm_report.max_velocity
        self.max_power = wm_report.max_power
        self.initial_mean_velocity = wm_report.initial_velocity
        self.last_mean_velocity = wm_report.last_velocity
        self.inc_mean_velocity = wm_report.inc_velocity
        self.total_lifting_time = wm_report.sum_rep_duration 

        self.convert_datatype()

        return WorkoutSetReportDTO(self.set, self.weight, self.total_reps, self.volume, 
                                   self.mean_velocity, self.mean_power, self.max_velocity, self.max_power, 
                                   self.initial_mean_velocity, self.last_mean_velocity, self.inc_mean_velocity, self.total_lifting_time, 
                                   wm_report )

workoutSetReport = WorkoutSetReport()
