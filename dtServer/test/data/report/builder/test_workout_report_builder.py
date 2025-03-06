import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.report.builder.workout_report_builder import workoutReportBuilder

conn = make_database_connection()
db_proxy.initialize(conn)

def test_build_workout_report() : 
    workout_id = 1

    workout_report = workoutReportBuilder.build_workout_report(workout_id)
    
    print(workout_report.as_dict())

def test_build_col_workout_report() : 
    user_id = 1
    exercise_library_id = 1

    workout_reports = workoutReportBuilder.build_recent_workout_reports_by_exercise_library(user_id, exercise_library_id)

    print(workout_reports.as_dict())

def test_build_recent_workout_reports_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1

    reports = workoutReportBuilder.build_recent_workout_reports_by_exercise_library(user_id, exercise_library_id)

    print(reports.as_dict())

def test_build_recent_workout_reports_by_body_part() : 
    user_id = 1
    body_part_id = 4

    reports = workoutReportBuilder.build_recent_workout_reports_by_body_part(user_id, body_part_id)

    print(reports.as_dict())

def test_build_recent_workout_reports_by_equipment() : 
    user_id = 1
    equipment_id = 11

    reports = workoutReportBuilder.build_recent_workout_reports_by_equipment(user_id, equipment_id)

    print(reports.as_dict())

if __name__ == "__main__" : 
    test_build_workout_report()
    test_build_col_workout_report()
    test_build_recent_workout_reports_by_exercise_library()
    test_build_recent_workout_reports_by_body_part()
    test_build_recent_workout_reports_by_equipment()
