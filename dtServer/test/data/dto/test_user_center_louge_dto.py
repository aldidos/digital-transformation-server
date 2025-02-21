import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dto.app_lounge_dto import AppLoungeDTO

conn = make_database_connection()
db_proxy.initialize(conn)

def test_app_lounge() :     
    user_id = 1
    center_id = 1

    app_lounge = AppLoungeDTO(user_id, center_id)

    print( app_lounge.as_dict() )

test_app_lounge()