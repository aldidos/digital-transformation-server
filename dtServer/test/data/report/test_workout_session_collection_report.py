import sys
sys.path.append('.')

from dtServer.data.report.workout_session_collection_report import WokroutSessionCollectionReport
from dtServer.test.data.report.create_test_data import create_test_dataset
from datetime import datetime

def test_make_report() : 

    test_dataset = create_test_dataset(3, 3, 3, 10)

    from_date = datetime(2025, 2, 1)
    to_date = datetime(2025, 3, 1)

    report = WokroutSessionCollectionReport(from_date, to_date)
    report.make_report(test_dataset)

    print( report.as_dict() ) 

test_make_report()