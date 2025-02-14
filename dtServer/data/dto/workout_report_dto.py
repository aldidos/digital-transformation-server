

class WorkoutReportDTO : 

    def __init__(self, total_workout_time, total_lifting_time, total_sets, total_volume, total_reps, avg_reps_pet_set, set_reports ) : 
        self.total_workout_time = total_workout_time
        self.total_lifting_time = total_lifting_time
        self.total_sets = total_sets
        self.total_volume = total_volume
        self.total_reps = total_reps
        self.avg_reps_pet_set = avg_reps_pet_set
        self.set_reports = set_reports        

    def get_with_dict(self) : 
        return {
            'total_workout_time' : self.total_workout_time, 
            'total_lifting_time' : self.total_lifting_time, 
            'total_sets' : self.total_sets, 
            'total_volume' : self.total_volume, 
            'total_reps' : self.total_reps, 
            'avg_reps_pet_set' : self.avg_reps_pet_set, 
            'set_reports' : self.set_reports
        }