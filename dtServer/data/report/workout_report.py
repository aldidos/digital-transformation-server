import pandas as pd
from dtServer.data.report.workout_set_report import workoutSetReport
from dtServer.data.dto.workout_report_dto import WorkoutReportDTO

class WorkoutReport : 

    def make_report(self, workout, df : pd.DataFrame ) : 

        total_sets = df['set'].drop_duplicates().count()
        total_volume = 0
        total_reps = 0
        total_lifting_time = 0

        list_set_reports = []

        groups = df.groupby([ 'set', 'weight', 'total_reps', 'set_start_time', 'set_end_time', 'res_start_time', 'res_end_time'])
        for name, df_group in groups : 
            workout_set = {
                'set' : name[0], 
                'weight' : name[1],
                'total_reps' : name[2]
            }

            workout_set_report = workoutSetReport.make_report(workout_set, df_group)            
            total_volume = total_volume + workout_set_report.volume
            total_reps = total_reps + workout_set_report.total_reps
            
            total_lifting_time = total_lifting_time + workout_set_report.workout_metric_report['sum_rep_duration']  ####

            list_set_reports.append( workout_set_report.get_with_dict() )

        total_sets = int(total_sets)
        total_volume = float(total_volume)
        avg_reps_pet_set = total_reps / total_sets

        total_workout_time = workout['end_time'] - workout['start_time']
        total_workout_time = total_workout_time.total_seconds()

        return WorkoutReportDTO(total_workout_time, total_lifting_time, total_sets, total_volume, total_reps, avg_reps_pet_set, list_set_reports )
        
workoutReport = WorkoutReport()