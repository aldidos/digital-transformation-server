from dtServer.data.report.workout_report import workoutReport
from dtServer.data.dto.workout_reports_dto import WorktoutReportsDTO

class WorkoutReports : 

    def __init__(self) : 
        self.list_workout_reports = []

    def make_report(self, list_dataset) : 
        for dataset in list_dataset : 
            workout = dataset['workout']
            workout_metrics = dataset['workout_metrics']

            workout_report = workoutReport.make_report(workout, workout_metrics)

            self.list_workout_reports.append( {
                'date' : workout['date'].isoformat(), 
                'workout_report' : workout_report.as_dict()
            })

        return WorktoutReportsDTO(self.list_workout_reports)
    
workoutReports = WorkoutReports()