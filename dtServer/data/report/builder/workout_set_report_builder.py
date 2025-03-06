from dtServer.data.report.workout_set_report import WorkoutSetReport
from dtServer.data.dao.workout.workout_report_data_dao import workoutReportDao
import pandas as pd

class WorkoutSetReportBuilder : 

    def build_recent_workout_set_report_by_exercise_library(self, user_id, exercise_library_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_exercise_library(user_id, exercise_library_id, set)
        return self.create_workout_set_report(workoutset['id'], dataset)
    
    def build_recent_workout_set_report_by_body_part(self, user_id, body_part_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_bodypart(user_id, body_part_id, set)
        return self.create_workout_set_report(workoutset['id'], dataset)
    
    def build_recent_workout_set_report_by_equipment(self, user_id, equipment_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_equipment(user_id, equipment_id, set)
        return self.create_workout_set_report(workoutset['id'], dataset)
    
    def build_workout_set_report(self, workout_id, workout_set_id) : 
        workoutset, dataset = workoutReportDao.get_workout_set_data(workout_set_id)
        return self.create_workout_set_report(workout_set_id, dataset)
    
    def create_workout_set_report(self, workout_set_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        df = df.drop(columns=['exercise_library_id', 'exercise_library', 'body_part', 'body_part']).drop_duplicates()
        
        workout_set_report = WorkoutSetReport(workout_set_id)
        workout_set_report.make_report(df)

        return workout_set_report

workoutSetReportBuilder = WorkoutSetReportBuilder()