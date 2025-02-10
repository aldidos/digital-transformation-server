from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao

class MachAppBaseData : 

    def get_data(self, user_id, center_equipment_id) : 
        with db_proxy.atomic() : 
            user = userDao.select_by_id(user_id)
            center_equipment = centerEquipmentDao.get_by_id(center_equipment_id)

            return {
                'user' : user, 
                'center_equipment' : center_equipment
            }