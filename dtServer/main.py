import sys
sys.path.append('./')

from dtServer.app import *
from dtServer.api.centers_api import *
from dtServer.api.users_api import *
from dtServer.api.base_api import *

if __name__ == '__main__' : 
     address = sys.argv[1]
     port = sys.argv[2]
     app.run(address, port=port, debug=True)