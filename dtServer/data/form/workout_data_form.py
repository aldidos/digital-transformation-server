
class WorkoutSetMetricsDTO : 

    def __init__(self, data : dict) : 
        self.data = data

    def get_workout_set(self) : 
        return self.data['workout_set']
    
    def get_workout_metrics(self) : 
        return self.data['workout_metrics']