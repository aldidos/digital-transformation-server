from dtServer.data.dto.workout_metric_report_dto import WorkoutMetricReportDTO

class WorkoutSetReportDTO : 

    def __init__(self, set, weight, total_reps, volume, mean_velocity, mean_power, max_velocity, max_power, initial_mean_velocity, last_mean_velocity, inc_mean_velocity, total_lifting_time, workout_metric_report : WorkoutMetricReportDTO ) : 
        self.set = set
        self.weight = weight
        self.total_reps = total_reps
        self.volume = volume 
        self.mean_velocity = mean_velocity
        self.mean_power = mean_power
        self.max_velocity = max_velocity
        self.max_power = max_power
        self.initial_mean_velocity = initial_mean_velocity
        self.last_mean_velocity = last_mean_velocity
        self.inc_mean_velocity = inc_mean_velocity
        self.total_lifting_time = total_lifting_time

        self.workout_metric_report = workout_metric_report

    def as_dict(self) : 
        return {
            'set' : self.set, 
            'weight' : self.weight, 
            'total_reps' : self.total_reps, 
            'volume' : self.volume, 
            'mean_velocity' : self.mean_velocity, 
            'mean_power' : self.mean_power, 
            'max_velocity' : self.max_velocity, 
            'max_power' : self.max_power, 
            'initial_mean_velocity' : self.initial_mean_velocity, 
            'last_mean_velocity' : self.last_mean_velocity, 
            'inc_mean_velocity' : self.inc_mean_velocity, 
            'total_lifting_time' : self.total_lifting_time, 

            'workout_metric_report' : self.workout_metric_report.as_dict()
        }