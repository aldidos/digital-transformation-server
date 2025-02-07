import pandas as pd

class StatWorkoutMetric : 
    def __init__(self) : 
        self.attr_weight = 'weight'
        self.attr_volume = 'volume'
        self.attr_peak_velocity = 'peak_velocity'
        self.attr_mean_velocity = 'mean_velocity'
        self.attr_peak_power = 'peak_power'
        self.attr_mean_power = 'mean_power'
        self.attr_height = 'height'
        self.attr_power = 'power'
        self.data_attrs = [self.attr_weight, self.attr_volume, self.attr_peak_velocity, self.attr_mean_velocity, self.attr_peak_power, self.attr_mean_power, self.attr_height, self.attr_power ]

    def extract_result(self, agg_result) : 
        weight = float( agg_result[ self.attr_weight ] )
        volume = float( agg_result[ self.attr_volume ] )
        peak_velocity = float( agg_result[ self.attr_peak_velocity ] )
        mean_velocity = float( agg_result[ self.attr_mean_velocity ] )
        peak_power = float( agg_result[ self.attr_peak_power ] )
        mean_power = float( agg_result[ self.attr_mean_power ] )
        height = float( agg_result[ self.attr_height ] )
        power = float( agg_result[ self.attr_power ] )
        
        return {
                'weight' : weight, 
                'volume' : volume, 
                'peak_velocity' : peak_velocity, 
                'mean_velocity' : mean_velocity, 
                'peak_power' : peak_power,
                'mean_power' : mean_power, 
                'height' : height, 
                'power' : power
                }
    
    def workout_metric_stat(self, df) : 
        agg_result = df[ self.data_attrs ].agg([ 'max', 'mean', 'sum' ])
        stat_sum = self.extract_result( agg_result.loc['sum'] )
        stat_max = self.extract_result( agg_result.loc['max'] )
        stat_mean = self.extract_result( agg_result.loc['mean'] ) 

        return {
            'sum' : stat_sum, 
            'max' : stat_max, 
            'mean' : stat_mean,
        }
    
    def temp_1(self, df : pd.DataFrame) : ####
        groups = df.groupby(['date', 'exercise_library_name', 'body_part_name', 'set'])
        result = []
        for group_name, group_df in groups :        
            wm_stat = self.workout_metric_stat( group_df ) 

            date = group_name[0].isoformat()
            exercise_name = group_name[1]
            set = int(group_name[2])
            
            wm_stat['date'] = date
            wm_stat['exercise_name'] = exercise_name
            wm_stat['set'] = set 

            result.append( wm_stat )

        return result
    
    def temp_2(self, df : pd.DataFrame ) :
        pass

    def stat_summary(self, dataset) : 
        df = pd.DataFrame(dataset)
        
        return []

stat_workout_metric = StatWorkoutMetric()