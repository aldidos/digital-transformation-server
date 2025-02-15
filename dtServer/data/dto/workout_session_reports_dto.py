

class WorkoutSessionReportsDTO : 

    def __init__(self, total_volume, total_exercise_libraries, total_workout_time, list_workout_session_reports) : 
        self.total_volume = total_volume
        self.total_exercise_libraries = total_exercise_libraries
        self.total_workout_time = total_workout_time
        self.list_workout_session_reports = list_workout_session_reports

    def as_dict(self) :

        return {
            'total_volume' : self.total_volume, 
            'total_exercise_libraries' : self.total_exercise_libraries, 
            'total_workout_time' : self.total_workout_time, 
            'list_workout_session_reports' : self.list_workout_session_reports, 
        }           

    