
class WeeklyWorkoutSummary : 

    def __init__(self) : 
        self.total_workout_volume = 0
        self.total_workout_time = 0
        self.total_running_distance = 0

    def as_dict(self) : 
        return {
            'total_workout_volume' : self.total_workout_volume,
            'total_workout_time' : self.total_workout_time,
            'total_running_distance' : self.total_running_distance
        }