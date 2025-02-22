
class WeeklyWorkoutSummary : 

    def __init__(self, total_workout_volume = 0, total_workout_time = 0, total_running_distance = 0) : 
        self.total_workout_volume = total_workout_volume
        self.total_workout_time = total_workout_time
        self.total_running_distance = total_running_distance

    def as_dict(self) : 
        self.total_workout_volume = float(self.total_workout_volume)
        self.total_running_distance = float(self.total_running_distance)

        return {
            'total_workout_volume' : self.total_workout_volume,
            'total_workout_time' : self.total_workout_time,
            'total_running_distance' : self.total_running_distance
        }