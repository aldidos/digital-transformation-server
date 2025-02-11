from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao

class MachinAppBaseDataTrans : 

    def get_data(self, user_id, center_equipment_id, workout_session_id) : 
        with db_proxy.atomic() : 
            user = userDao.select_by_id(user_id)
            center_equipment = centerEquipmentDao.get_by_id(center_equipment_id)
            wokrout_session = workoutSessionDao.select_by_id(workout_session_id)

            return {
                'user' : user, 
                'center_equipment' : center_equipment, 
                'workout_session' : wokrout_session
            }
        
machinAppBaseDataTrans = MachinAppBaseDataTrans()