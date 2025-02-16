from dtServer.data.dto.workout_report_dto import WorkoutReportDTO

class WorktoutCollectionReportDTO : 

    def __init__(self, total_volume, total_workout_time, total_workouts, total_sets, workout_reports : list[WorkoutReportDTO]  ) : 
        self.total_volume = total_volume
        self.total_workout_time = total_workout_time
        self.total_workouts = total_workouts
        self.total_sets = total_sets
        self.workout_reports = workout_reports

    def as_dict(self) : 
        return {
            'total_volume' : self.total_volume,
            'total_workout_time' : self.total_workout_time,
            'total_workouts' : self.total_workouts,
            'total_sets' : self.total_sets,
            'workout_reports' : [ d for d in self.workout_reports]
        }
    