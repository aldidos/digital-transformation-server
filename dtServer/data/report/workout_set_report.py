import pandas as pd
from dtServer.data.report.workout_metric_report import workoutMetricReport
from dtServer.data.dto.workout_set_report_dto import WorkoutSetReportDTO

class WorkoutSetReport : 

    def __init__(self) : 
        self.volume = 0 
        self.set = 0
        self.weight = 0
        self.total_reps = 0

    def convert_datatype(self) : 
        self.volume = float(self.volume)
        self.set = int(self.set)
        self.weight = float(self.weight)
        self.total_reps = int(self.total_reps)

    def make_report(self, set_info, workout_metrics : dict ) : 
        df = pd.DataFrame(workout_metrics)
        self.set = set_info['set']
        self.weight = set_info['weight']
        self.total_reps = set_info['total_reps']

        self.volume = self.weight * self.total_reps
        wm_report = workoutMetricReport.make_report(df)

        self.convert_datatype()

        return WorkoutSetReportDTO(self.set, self.weight, self.total_reps, self.volume, wm_report.get_data_with_dict() )

workoutSetReport = WorkoutSetReport()
