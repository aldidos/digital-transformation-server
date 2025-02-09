import sys
sys.path.append('./')

from dtServer.api import *
from dtServer.api.centers import *
from dtServer.api.users import *
from dtServer.api.base import *

if __name__ == '__main__' : 
     app.run('localhost', port=5000, debug=True)