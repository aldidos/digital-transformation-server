from dtServer.data.dto.workout_report_dto import WorkoutReportDTO

class WorkoutSessionReportDTO : 

    def __init__(self, total_volume, total_sets, total_workout_time, total_workouts, list_workout_reports : list[WorkoutReportDTO]) : 
        self.total_volume = total_volume
        self.total_sets = total_sets
        self.total_workout_time = total_workout_time
        self.total_workouts = total_workouts
        self.list_workout_reports = list_workout_reports

    def as_dict(self) : 
        return {
            'total_sets' : self.total_sets,
            'total_workout_time' : self.total_workout_time,
            'total_workouts' : self.total_workouts,
            'list_workout_reports' : [d.as_dict() for d in self.list_workout_reports]
        }