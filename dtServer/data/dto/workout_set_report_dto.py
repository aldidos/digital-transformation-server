
class WorkoutSetReportDTO : 

    def __init__(self, set, weight, total_reps, volume, workout_metric_report ) : 
        self.set = set
        self.weight = weight
        self.total_reps = total_reps
        self.volume = volume

        self.workout_metric_report = workout_metric_report

    def get_with_dict(self) : 
        return {
            'set' : self.set, 
            'weight' : self.weight, 
            'total_reps' : self.total_reps, 
            'volume' : self.volume, 
            'workout_metric_report' : self.workout_metric_report
        }