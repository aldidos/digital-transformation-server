import sys
sys.path.append('./')

from dtServer.app import *
from dtServer.api.centers import *
from dtServer.api.users import *
from dtServer.api.base import *

if __name__ == '__main__' : 
     address = sys.argv[1]
     port = sys.argv[2]
     app.run(address, port=port, debug=True)