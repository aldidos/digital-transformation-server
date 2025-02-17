from dtServer.data.dto.workout_set_report_dto import WorkoutSetReportDTO

class WorkoutReportDTO : 

    def __init__(self, total_workout_time, total_lifting_time, total_sets, total_volume, 
                 total_reps, avg_reps_pet_set, avg_weight, burned_kcl, intensity, exercise_libraries, body_parts, set_reports : list[WorkoutSetReportDTO] ) : 
        self.total_workout_time = total_workout_time
        self.total_lifting_time = total_lifting_time
        self.total_sets = total_sets
        self.total_volume = total_volume
        self.total_reps = total_reps
        self.avg_reps_pet_set = avg_reps_pet_set
        self.set_reports = set_reports     
        self.avg_weight = avg_weight
        self.burned_kcl = burned_kcl
        self.intensity = intensity
        self.exercise_libraries = exercise_libraries
        self.body_parts = body_parts

    def as_dict(self) : 
        return {
            'total_workout_time' : self.total_workout_time, 
            'total_lifting_time' : self.total_lifting_time, 
            'total_sets' : self.total_sets, 
            'total_volume' : self.total_volume, 
            'total_reps' : self.total_reps, 
            'avg_reps_pet_set' : self.avg_reps_pet_set, 
            'avg_weight' : self.avg_weight,
            'burned_kcl' : self.burned_kcl,
            'intensity' : self.intensity,
            'exercise_libraries' : self.exercise_libraries,
            'body_parts' : self.body_parts,
            'set_reports' : [ d.as_dict() for d in self.set_reports]
        }