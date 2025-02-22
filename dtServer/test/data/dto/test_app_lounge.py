import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dto.app_lounge_dto import AppLoungeDTO
from datetime import datetime, timedelta

conn = make_database_connection()
db_proxy.initialize(conn)

def test_app_lounge() :     
    user_id = 1
    center_id = 1
    to_date = datetime.today()
    from_date = to_date - timedelta(7)

    app_lounge = AppLoungeDTO(user_id, center_id, from_date, to_date)

    print( app_lounge.as_dict() )

test_app_lounge()