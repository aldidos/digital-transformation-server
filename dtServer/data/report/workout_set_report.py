import pandas as pd
from dtServer.data.report.workout_metric_report import workoutMetricReport
from dtServer.data.dto.workout_set_report_dto import WorkoutSetReportDTO

class WorkoutSetReport : 

    def make_report(self, set_info, df_workout_metrics : pd.DataFrame) : 
        set = int(set_info['set'])
        weight = float(set_info['weight'])
        total_reps = int(set_info['total_reps'])

        volume = weight * total_reps
        volume = float(volume)        

        wm_report = workoutMetricReport.make_report(df_workout_metrics)

        return WorkoutSetReportDTO(set, weight, total_reps, volume, wm_report.get_data_with_dict() )

workoutSetReport = WorkoutSetReport()
