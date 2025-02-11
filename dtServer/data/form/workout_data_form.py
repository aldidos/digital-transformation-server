
class WorkoutDataForm : 

    def __init__(self, data) : 
        self.workout = data['workout']
        self.workout_sets = data['workout_sets']

    def get_workout(self) : 
        return self.workout

    def get_workout_sets(self) : 
        return self.workout_sets 