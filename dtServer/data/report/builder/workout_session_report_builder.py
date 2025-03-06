from dtServer.data.dao.workout.workout_report_data_dao import workoutReportDao
from dtServer.data.report.workout_session_report import WokroutSessionReport
from dtServer.data.report.workout_session_collection_report import WokroutSessionCollectionReport
import pandas as pd

class WorkoutSessionReportBuilder : 

    def build_date_period_workout_session_reports(self, user_id, from_date, to_date ) : 
        dataset = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
        return self.create_workout_session_report_collection(from_date, to_date, dataset)
    
    def build_date_period_workout_session_reports(self, user_id, from_date, to_date ) : 
        dataset = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
        return self.create_workout_session_report_collection(from_date, to_date, dataset)
    
    def build_workout_session_report(self, workout_session_id) : 
        dataset = workoutReportDao.get_workoutsession_data(workout_session_id)
        return self.create_workout_session_report(workout_session_id, dataset)
    
    def create_workout_session_report(self, workout_session_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)                
        workout_session_report = WokroutSessionReport(workout_session_id)
        workout_session_report.make_report(df)

        return workout_session_report
    
    def create_workout_session_report_collection(self, from_date, to_date, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        workout_session_reports = WokroutSessionCollectionReport(from_date, to_date)
        workout_session_reports.make_report(df)

        return workout_session_reports
    
workoutSessionReportBuilder = WorkoutSessionReportBuilder()