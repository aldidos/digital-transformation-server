import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.report.workout_session_report import WokroutSessionReport
import pandas as pd

conn = make_database_connection()
db_proxy.initialize(conn)

workout_session_id = 1

data = workoutMetricDao.select_workout_session_level_data(workout_session_id)

df = pd.DataFrame(data)

wsr = WokroutSessionReport(workout_session_id)
wsr.make_report( df )

print(wsr.as_dict())