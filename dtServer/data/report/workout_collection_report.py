from dtServer.data.report.workout_report import workoutReport
from dtServer.data.dto.workout_collection_report_dto import WorktoutCollectionReportDTO

class WorkoutColectionReport : 

    def __init__(self) : 
        self.total_volume = 0 
        self.total_workout_time = 0
        self.total_workouts = 0
        self.total_sets = 0
        self.list_workout_reports = []

    def make_report(self, list_dataset) : 
        self.total_workouts = len(list_dataset)

        for dataset in list_dataset : 
            workout = dataset['workout']
            workout_metrics = dataset['workout_metrics']

            workout_report = workoutReport.make_report(workout, workout_metrics)

            self.total_volume = self.total_volume + workout_report.total_volume
            self.total_workout_time = self.total_workout_time + workout_report.total_workout_time            
            self.total_sets = self.total_sets + workout_report.total_sets

            self.list_workout_reports.append( {
                'date' : workout['date'].isoformat(), 
                'workout_report' : workout_report.as_dict()
            })        

        return WorktoutCollectionReportDTO(self.total_volume, self.total_workout_time, self.total_workouts, self.total_sets, self.list_workout_reports)
    
workoutColReport = WorkoutColectionReport()