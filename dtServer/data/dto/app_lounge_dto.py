from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_centermember_dao import userCenterMemberDao
from dtServer.data.dto.weekly_workout_summary import WeeklyWorkoutSummary

class AppLoungeDTO : 

    def __init__(self, user_id, center_id) : 
        self.init(user_id, center_id)        

    def init(self, user_id, center_id) : 
        with db_proxy.atomic() : 
            user_center_member = userCenterMemberDao.get_by_user_and_center(user_id, center_id)
            self.user = user_center_member['user']
            self.center = user_center_member['center']
            self.center_member = user_center_member['center_member']

            self.center_reg_from = self.center_member['reg_from']
            self.center_reg_to = self.center_member['reg_to']
            self.last_visit_date = self.center_member['visit_date']

            self.weekly_workout_summary = WeeklyWorkoutSummary()

    def as_dict(self) : 
        return {
            'user' : self.user, 
            'center' : self.center, 
            'center_member' : self.center_member, 
            'center_reg_from' : self.center_reg_from, 
            'center_reg_to' : self.center_reg_to, 
            'last_visit_date' : self.last_visit_date,             
            'weekly_workout_summary' : self.weekly_workout_summary.as_dict()
        }

