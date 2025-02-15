
class WorktoutReportsDTO : 

    def __init__(self, workout_reports) : 
        self.workout_reports = workout_reports

    def as_dict(self) : 
        return {
            'workout_reports' : self.workout_reports
        }