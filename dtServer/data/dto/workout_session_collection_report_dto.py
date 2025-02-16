from dtServer.data.dto.workout_session_report_dto import WorkoutSessionReportDTO

class WorkoutSessionCollectionReportDTO : 

    def __init__(self, total_volume, total_workout_time, total_sets, total_workouts, list_workout_session_reports : list[WorkoutSessionReportDTO]) : 
        self.total_volume = total_volume
        self.total_workout_time = total_workout_time
        self.total_sets = total_sets
        self.total_workouts = total_workouts
        self.list_workout_session_reports = list_workout_session_reports

    def as_dict(self) :

        return {
            'total_volume' : self.total_volume, 
            'total_workout_time' : self.total_workout_time, 
            'total_sets' : self.total_sets, 
            'total_workouts' : self.total_workouts,
            'list_workout_session_reports' : [d for d in self.list_workout_session_reports]
        }           

    