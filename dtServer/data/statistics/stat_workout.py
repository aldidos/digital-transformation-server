import pandas as pd

class StatWorkout : 

    def __init__(self) :
        self.data_attrs = []

    def stat(self, list_data) : 
        df = pd.DataFrame(list_data)

        df['diff_time'] = df['end_time'] - df['start_time']
        sum_diff_time = df['diff_time'].sum()
        total_workout_second = sum_diff_time.total_seconds()
        count_exercise_libraries = int(df['exercise_library_name'].count() ) 

        return { 'total_workout_second' : total_workout_second, 'num_exercise_libraries' : count_exercise_libraries }

statWorkout = StatWorkout()