import sys
sys.path.append('.')

from dtServer.data.report.workout_collection_report import WorkoutColectionReport
from dtServer.test.data.report.create_test_data import create_test_dataset

def test_make_report() : 

    test_dataset = create_test_dataset(1, 3, 3, 10)

    report = WorkoutColectionReport()
    report.make_report(test_dataset)

    print( report.as_dict() ) 

test_make_report()