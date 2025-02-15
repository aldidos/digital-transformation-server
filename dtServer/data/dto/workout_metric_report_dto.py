
class WorkoutMetricReportDTO : 

    def __init__(self, mean_velocity, mean_power, max_velocity, max_power,
                 initial_velocity, last_velocity, inc_velocity, sum_rep_duration, 
                 recommended_weight = None) : 
                
        self.mean_velocity = mean_velocity
        self.mean_power = mean_power
        self.max_velocity = max_velocity
        self.max_power = max_power
        self.initial_velocity = initial_velocity
        self.inc_velocity = inc_velocity
        self.last_velocity = last_velocity
        self.sum_rep_duration = sum_rep_duration 
        
        if recommended_weight :
            self.recommended_weight = recommended_weight        

    def get_mean_velocity(self) : 
        return self.mean_velocity
    
    def get_mean_power(self) : 
        return self.mean_power

    def get_data_with_dict(self) : 
        return {
            'mean_velocity' : self.mean_velocity, 
            'mean_power' : self.mean_power,
            'max_velocity' : self.max_velocity, 
            'max_power' : self.max_power,
            'initial_velocity' : self.initial_velocity,
            'inc_velocity' : self.inc_velocity,
            'last_velocity' : self.last_velocity, 
            'sum_rep_duration' : self.sum_rep_duration
        }
        