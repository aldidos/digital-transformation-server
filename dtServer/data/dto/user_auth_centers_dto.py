from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.user_center_dao import userCenterDao

class UserAuthCentersDTO : 

    def __init__(self, user_id) : 
        self.get_data(user_id)

    def get_authenticated_centers(self, user_centers) : 
        centers = []        
        for user_center in user_centers : 
            centers.append( user_center['center'] ) 
        return centers

    def get_data(self, user_id) :
        with db_proxy.atomic() :             
            user = userDao.select_by_id(user_id) 
            authenticated_centers = self.get_authenticated_centers( userCenterDao.get_by_user( user_id ) )

            self.user = user, 
            self.authenticated_centers = authenticated_centers
            return {
                'user' : user,                 
                'authenticated_centers' : authenticated_centers
            }
    
    def as_dict(self) : 
        return {
            'user' : self.user,                 
            'authenticated_centers' : self.authenticated_centers
        }