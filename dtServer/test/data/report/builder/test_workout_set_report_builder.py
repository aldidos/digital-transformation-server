import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.report.builder.workout_set_report_builder import workoutSetReportBuilder

conn = make_database_connection()
db_proxy.initialize(conn)

def test_build_workout_set_report() : 
    workout_id = 1
    workout_set_id = 1

    workout_set_report = workoutSetReportBuilder.build_workout_set_report(workout_id, workout_set_id)

    print(workout_set_report.as_dict())

def test_build_recent_workout_set_report_by_exercise_library() : 
    user_id = 1
    exercise_library_id = 1
    set = 1

    recent_exercise_library_set_report = workoutSetReportBuilder.build_recent_workout_set_report_by_exercise_library(user_id, exercise_library_id, set)    

    print(recent_exercise_library_set_report.as_dict())

def test_build_recent_workout_set_report_by_body_part() : 
    user_id = 1
    body_part_id = 4
    set = 1

    recent_exercise_library_set_report = workoutSetReportBuilder.build_recent_workout_set_report_by_body_part(user_id, body_part_id, set)    

    print(recent_exercise_library_set_report.as_dict())

def test_build_recent_workout_set_report_by_equipment() : 
    user_id = 1
    equipment_id = 11
    set = 1

    recent_exercise_library_set_report = workoutSetReportBuilder.build_recent_workout_set_report_by_equipment(user_id, equipment_id, set)    

    print(recent_exercise_library_set_report.as_dict())

if __name__ == "__main__" : 
    test_build_workout_set_report()
    test_build_recent_workout_set_report_by_exercise_library()
    test_build_recent_workout_set_report_by_body_part()
    test_build_recent_workout_set_report_by_equipment()
