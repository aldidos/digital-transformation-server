
class WorkoutMetricReportDTO : 

    def __init__(self, mean_velocity, mean_power, max_velocity, max_power,
                 initial_velocity, last_velocity, inc_velocity, total_rep_duration, 
                 total_rep_duration_con, total_rep_duration_ecc, total_top_stay_duration, total_bottom_stay_duration,
                 recommended_weight = None) : 
                
        self.mean_velocity = mean_velocity
        self.mean_power = mean_power
        self.max_velocity = max_velocity
        self.max_power = max_power
        self.initial_velocity = initial_velocity        
        self.last_velocity = last_velocity
        self.inc_velocity = inc_velocity
        self.total_rep_duration = total_rep_duration 
        self.total_rep_duration_con = total_rep_duration_con
        self.total_rep_duration_ecc = total_rep_duration_ecc
        self.total_top_stay_duration = total_top_stay_duration
        self.total_bottom_stay_duration = total_bottom_stay_duration
        
        if recommended_weight :
            self.recommended_weight = recommended_weight        

    def get_mean_velocity(self) : 
        return self.mean_velocity
    
    def get_mean_power(self) : 
        return self.mean_power

    def as_dict(self) : 
        return {
            'mean_velocity' : self.mean_velocity, 
            'mean_power' : self.mean_power,
            'max_velocity' : self.max_velocity, 
            'max_power' : self.max_power,
            'initial_velocity' : self.initial_velocity,
            'inc_velocity' : self.inc_velocity,
            'last_velocity' : self.last_velocity, 
            'total_rep_duration' : self.total_rep_duration,
            'total_rep_duration_con' : self.total_rep_duration_con,
            'total_rep_duration_ecc' : self.total_rep_duration_ecc,
            'total_top_stay_duration' : self.total_top_stay_duration,
            'total_bottom_stay_duration' : self.total_bottom_stay_duration

        }
        