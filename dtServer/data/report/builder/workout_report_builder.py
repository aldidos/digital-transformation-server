from dtServer.data.dao.workout_report_data_dao import workoutReportDao
from dtServer.data.report.workout_session_report import WokroutSessionReport
from dtServer.data.report.workout_report import WorkoutReport
from dtServer.data.report.workout_set_report import WorkoutSetReport
from dtServer.data.report.workout_collection_report import WorkoutColectionReport
from dtServer.data.report.workout_session_collection_report import WokroutSessionCollectionReport

class WorkoutReportBuilder : 

    def build_recent_exercise_library_set_report(user_id, exercise_library_id, set) : 
        workout_set, workout_metric = workoutReportDao.get_recent_set_data(user_id, exercise_library_id, set)
        if not workout_set : 
            return None

        workout_set_report = WorkoutSetReport()
        workout_set_report.make_report(workout_set, workout_metric)

        return workout_set_report

    def build_workout_session_report(workout_session_id) : 
        workout_session, dataset = workoutReportDao.get_workoutsession_data(workout_session_id)
        if not workout_session : 
            return None
                
        workout_session_report = WokroutSessionReport()
        workout_session_report.make_report(dataset)

        return workout_session_report

    def build_workout_report(workout_id) : 
        workout, dataset = workoutReportDao.get_workout_data(workout_id)
        if not workout : 
            return None
        
        workout_report = WorkoutReport()
        workout_report.make_report(workout, dataset)
        
        return workout_report

    def build_workout_set_report(workout_id, workout_set_id) : 
        workout_set, dataset = workoutReportDao.get_set_data(workout_id, workout_set_id)
        if not workout_set : 
            return None
        
        workout_set_report = WorkoutSetReport()
        workout_set_report.make_report(workout_set, dataset)

        return workout_set_report

    def build_recent_exerciselib_workout_reports(user_id, exercise_library_id) : 
        list_dataset = workoutReportDao.get_recent_workout_data_by_user_and_exercise(user_id, exercise_library_id)
        if not list_dataset : 
            return None
        
        workout_reports = WorkoutColectionReport()
        workout_reports.make_report(list_dataset)

        return workout_reports

    def build_date_period_workout_session_reports( user_id, from_date, to_date ) : 
        list_dataset = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
        if not list_dataset : 
            return None
        
        workout_session_reports = WokroutSessionCollectionReport()
        workout_session_reports.make_report(list_dataset)

        return workout_session_reports