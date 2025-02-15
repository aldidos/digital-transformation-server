from dtServer.data.dao.workout_report_data_dao import workoutReportDao
from dtServer.data.report.workout_session_report import workoutSessionReport
from dtServer.data.report.workout_report import workoutReport
from dtServer.data.report.workout_set_report import workoutSetReport
from dtServer.data.report.workout_reports import workoutReports
from dtServer.data.report.workout_session_reports import workoutSessionReports

class WorkoutReportBuilder : 

    def build_recent_exercise_library_set_report(user_id, exercise_library_id, set) : 
        workout_set, workout_metric = workoutReportDao.get_recent_set_data(user_id, exercise_library_id, set)
        if not workout_set : 
            return None

        workout_set_report = workoutSetReport.make_report(workout_set, workout_metric)
        return workout_set_report.as_dict()

    def build_workout_session_report(workout_session_id) : 
        workout_session, dataset = workoutReportDao.get_workoutsession_data(workout_session_id)
        if not workout_session : 
            return None
                
        workout_session_report = workoutSessionReport.make_report(dataset)

        return workout_session_report.as_dict()

    def build_workout_report(workout_id) : 
        workout, dataset = workoutReportDao.get_workout_data(workout_id)
        if not workout : 
            return None
        
        workout_report = workoutReport.make_report(workout, dataset)
        
        return workout_report.as_dict()

    def build_workout_set_report(workout_id, workout_set_id) : 
        workout_set, dataset = workoutReportDao.get_set_data(workout_id, workout_set_id)
        if not workout_set : 
            return None
        
        workout_set_report = workoutSetReport.make_report(workout_set, dataset)

        return workout_set_report.as_dict()

    def build_workout_reports(user_id, exercise_library_id) : 
        list_dataset = workoutReportDao.get_recent_workout_data_by_user_and_exercise(user_id, exercise_library_id)
        if not list_dataset : 
            return None
        
        workout_reports = workoutReports.make_report(list_dataset)    

        return workout_reports.as_dict()

    def build_workout_session_reports( user_id, from_date, to_date ) : 
        list_dataset = workoutReportDao.get_workout_sessions_by_dateperiod(user_id, from_date, to_date)
        if not list_dataset : 
            return None
        
        workout_session_reports = workoutSessionReports.make_report(list_dataset)

        return workout_session_reports.as_dict()