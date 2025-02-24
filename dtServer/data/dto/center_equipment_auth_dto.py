from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao

class CenterEquipmentAuthDTO : 

    def __init__(self, user_id, workout_session_id, center_equipment_id) : 
        with db_proxy.atomic() : 
            self.user = userDao.select_by_id( user_id )
            self.workout_session = workoutSessionDao.select_by_id( workout_session_id )
            self.center_equipment = centerEquipmentDao.get_by_id(center_equipment_id ) 
            self.center_equipment['usage'] = True
            self.center_equipment = centerEquipmentDao.save( self.center_equipment)

    def as_dict(self) : 
            return {
                'user' : self.user, 
                'workout_session' : self.workout_session, 
                'center_equipment' : self.center_equipment
            }