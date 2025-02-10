from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.user_center_dao import userCenterDao
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao

class AppBaseData : 

    def get_authenticated_centers(self, user_centers) : 
        centers = []        
        for user_center in user_centers : 
            centers.append( user_center['center'] ) 
        return centers

    def get_data(self, user_id) :
        with db_proxy.atomic() :             
            user = userDao.select_by_id(user_id) 
            authenticated_centers = self.get_authenticated_centers( userCenterDao.get_by_user( user_id ) )

            return {
                'user' : user,                 
                'authenticated_centers' : authenticated_centers
            }