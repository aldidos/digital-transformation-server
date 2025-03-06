from dtServer.data.dao.workout.workout_report_data_dao import workoutReportDao
from dtServer.data.report.workout_session_report import WokroutSessionReport
from dtServer.data.report.workout_report import WorkoutReport
from dtServer.data.report.workout_set_report import WorkoutSetReport
from dtServer.data.report.workout_collection_report import WorkoutColectionReport
from dtServer.data.report.workout_session_collection_report import WokroutSessionCollectionReport
import pandas as pd

class WorkoutReportBuilder : 

    def build_recent_workout_set_report_by_exercise_library(user_id, exercise_library_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_exercise_library(user_id, exercise_library_id, set)
        return WorkoutReportBuilder.create_workout_set_report(workoutset['id'], dataset)
    
    def build_recent_workout_set_report_by_body_part(user_id, body_part_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_bodypart(user_id, body_part_id, set)
        return WorkoutReportBuilder.create_workout_set_report(workoutset['id'], dataset)
    
    def build_recent_workout_set_report_by_equipment(user_id, equipment_id, set) : 
        workoutset, dataset = workoutReportDao.get_recent_set_data_by_equipment(user_id, equipment_id, set)
        return WorkoutReportBuilder.create_workout_set_report(workoutset['id'], dataset)

    def build_workout_session_report(workout_session_id) : 
        dataset = workoutReportDao.get_workoutsession_data(workout_session_id)
        return WorkoutReportBuilder.create_workout_session_report(workout_session_id, dataset)

    def build_workout_report(workout_id) : 
        dataset = workoutReportDao.get_workout_data(workout_id)    
        return WorkoutReportBuilder.create_workout_report(workout_id, dataset)

    def build_workout_set_report(workout_id, workout_set_id) : 
        workoutset, dataset = workoutReportDao.get_workout_set_data(workout_set_id)
        return WorkoutReportBuilder.create_workout_set_report(workout_set_id, dataset)
        
    def build_recent_workout_reports_by_exercise_library(user_id, exercise_library_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_exercise(user_id, exercise_library_id)
        return WorkoutReportBuilder.create_workout_report_collection(dataset)        
    
    def build_recent_workout_reports_by_body_part(user_id, body_part_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_body_part(user_id, body_part_id)
        return WorkoutReportBuilder.create_workout_report_collection(dataset)        
    
    def build_recent_workout_reports_by_equipment(user_id, equipment_id) : 
        dataset = workoutReportDao.get_recent_workout_data_by_equipment(user_id, equipment_id)
        return WorkoutReportBuilder.create_workout_report_collection(dataset)
    
    def build_date_period_workout_session_reports( user_id, from_date, to_date ) : 
        dataset = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
        return WorkoutReportBuilder.create_workout_session_report_collection(from_date, to_date, dataset)
    
    def create_workout_session_report(workout_session_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)                
        workout_session_report = WokroutSessionReport(workout_session_id)
        workout_session_report.make_report(df)

        return workout_session_report
            
    def create_workout_report_collection(dataset) : 
        if not dataset : 
            return None

        df = pd.DataFrame(dataset)        
        workout_reports = WorkoutColectionReport()
        workout_reports.make_report(df)

        return workout_reports
    
    def create_workout_session_report_collection(from_date, to_date, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        workout_session_reports = WokroutSessionCollectionReport(from_date, to_date)
        workout_session_reports.make_report(df)

        return workout_session_reports 

    def create_workout_report(workout_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        df = df.drop(columns=['exercise_library_id', 'exercise_library', 'body_part', 'body_part']).drop_duplicates()
        
        workout_report = WorkoutReport(workout_id)
        workout_report.make_report(df)
        
        return workout_report
    
    def create_workout_set_report(workout_set_id, dataset) : 
        if not dataset : 
            return None
        
        df = pd.DataFrame(dataset)
        df = df.drop(columns=['exercise_library_id', 'exercise_library', 'body_part', 'body_part']).drop_duplicates()
        
        workout_set_report = WorkoutSetReport(workout_set_id)
        workout_set_report.make_report(df)

        return workout_set_report