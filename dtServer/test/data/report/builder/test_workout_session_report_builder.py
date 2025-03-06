import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.report.builder.workout_session_report_builder import workoutSessionReportBuilder

conn = make_database_connection()
db_proxy.initialize(conn)

def test_build_workout_session_report() : 
    workout_session_id = 1

    workout_session_report = workoutSessionReportBuilder.build_workout_session_report(workout_session_id)

    print( workout_session_report.as_dict() ) 

def test_build_date_period_workout_session_reports() : 
    user_id = 1
    from_date = '2025-01-01'
    to_date = '2025-03-01'

    workout_session_reports = workoutSessionReportBuilder.build_date_period_workout_session_reports(user_id, from_date, to_date)

    print(workout_session_reports.as_dict())

if __name__ == "__main__" : 
    test_build_workout_session_report()
    test_build_date_period_workout_session_reports()
