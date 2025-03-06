from dtServer.data.dao.workout.workout_report_data_dao import workoutReportDao
from dtServer.data.report.workout_report import WorkoutReport
from dtServer.data.report.workout_collection_report import WorkoutColectionReport
import pandas as pd

class WorkoutReportBuilder : 

    def build_workout_report(self, workout_id) : 
        dataset = workoutReportDao.get_workout_data(workout_id)    
        return self.create_workout_report(workout_id, dataset)

    def build_recent_workout_reports_by_exercise_library(self,user_id, exercise_library_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_exercise(user_id, exercise_library_id)
        return self.create_workout_report_collection(dataset)        
    
    def build_recent_workout_reports_by_body_part(self,user_id, body_part_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_body_part(user_id, body_part_id)
        return self.create_workout_report_collection(dataset)        
    
    def build_recent_workout_reports_by_equipment(self,user_id, equipment_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_equipment(user_id, equipment_id)
        return self.create_workout_report_collection(dataset)
    
    def create_workout_report_collection(self,dataset) : 
        if not dataset : 
            return None

        df = pd.DataFrame(dataset)
        workout_reports = WorkoutColectionReport()
        workout_reports.make_report(df)

        return workout_reports

    def create_workout_report(self,workout_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        df = df.drop(columns=['exercise_library_id', 'exercise_library', 'body_part', 'body_part']).drop_duplicates()
        
        workout_report = WorkoutReport(workout_id)
        workout_report.make_report(df)
        
        return workout_report

workoutReportBuilder = WorkoutReportBuilder()