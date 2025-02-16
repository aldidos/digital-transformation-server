import sys
sys.path.append('.')

from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao

conn = make_database_connection()
db_proxy.initialize(conn)

data = exerciseLibraryDao.select_by_equipment(16)

print(data)