import sys
sys.path.append('.')

from dtServer.data.report.workout_session_report import WokroutSessionReport
from dtServer.test.data.report.create_test_data import create_test_dataset

def test_make_report() : 

    test_data = create_test_dataset(1,3,3,10)

    workout_session_id = 1
    report = WokroutSessionReport(workout_session_id)
    report.make_report(test_data)
    print(report.as_dict())   


test_make_report()