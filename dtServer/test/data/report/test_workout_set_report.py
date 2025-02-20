import sys
sys.path.append('.')

from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.report.workout_set_report import WorkoutSetReport
from dtServer.test.data.report.create_test_data import create_test_dataset

def test_make_report() : 

    test_data = create_test_dataset(1,1,1,10)

    set_id = 1
    report = WorkoutSetReport(set_id)
    report.make_report(test_data)
    print(report.as_dict())   


test_make_report()