import pandas as pd
from dtServer.data.report.workout_set_report import workoutSetReport
from dtServer.data.dto.workout_report_dto import WorkoutReportDTO

class WorkoutReport : 

    def __init__(self) : 
        self.total_sets = 0
        self.total_volume = 0
        self.total_reps = 0
        self.total_lifting_time = 0
        self.avg_weight = 0
        self.avg_reps_pet_set = 0
        self.total_workout_time = 0 
        self.list_set_reports = []

    def conver_datatype(self) : 
        self.total_sets = int(self.total_sets)
        self.total_volume = float(self.total_volume)
        self.total_reps = int(self.total_reps)
        self.total_lifting_time = 0
        self.avg_weight = 0
        self.avg_reps_pet_set = float(self.avg_reps_pet_set)
        self.total_workout_time = float(self.total_workout_time)

    def make_report(self, workout, dataset ) : 
        df = pd.DataFrame(dataset)

        self.total_sets = df['set'].drop_duplicates().count()

        sum_weight = 0

        groups = df.groupby([ 'set', 'weight', 'total_reps', 'set_start_time', 'set_end_time', 'res_start_time', 'res_end_time'])
        for name, df_group in groups : 
            weight = name[1]
            total_reps = name[2]

            workout_set = {
                'set' : name[0], 
                'weight' : weight,
                'total_reps' : total_reps
            }

            workout_set_report = workoutSetReport.make_report(workout_set, df_group)            
            self.total_volume = self.total_volume + workout_set_report.volume
            self.total_reps = self.total_reps + total_reps
            self.total_lifting_time = self.total_lifting_time + workout_set_report.total_lifting_time
            sum_weight = sum_weight + weight

            self.list_set_reports.append( workout_set_report )

        self.avg_reps_pet_set = self.total_reps / self.total_sets
        self.avg_weight = sum_weight / self.total_sets
        self.total_workout_time = workout['end_time'] - workout['start_time'] 
        self.total_workout_time = self.total_workout_time.total_seconds()

        self.conver_datatype()
        return WorkoutReportDTO(self.total_workout_time, self.total_lifting_time, self.total_sets, self.total_volume, 
                                self.total_reps, self.avg_reps_pet_set, self.avg_weight,  self.list_set_reports 
                                )
       
workoutReport = WorkoutReport()