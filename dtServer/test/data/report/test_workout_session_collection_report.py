import sys
sys.path.append('.')

from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.report.workout_session_collection_report import WokroutSessionCollectionReport
from dtServer.test.data.report.create_test_data import create_test_dataset

def test_make_report() : 

    test_dataset = create_test_dataset(3, 3, 3, 10)

    report = WokroutSessionCollectionReport()
    report.make_report(test_dataset)

    print( report.as_dict() ) 

test_make_report()