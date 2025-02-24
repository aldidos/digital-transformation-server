from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_centermember_dao import userCenterMemberDao
from dtServer.data.dto.weekly_workout_summary import WeeklyWorkoutSummary
from dtServer.data.report.builder.workout_report_builder import WorkoutReportBuilder
from dtServer.util.datetime_util import timedelta_to_dhm_format
from datetime import timedelta

class AppLoungeDTO : 

    def __init__(self, user_id, center_id, from_date, to_date) : 
        self.init(user_id, center_id, from_date, to_date)

    def init(self, user_id, center_id, from_date, to_date) : 
        with db_proxy.atomic() : 
            user_center_member = userCenterMemberDao.get_by_user_and_center(user_id, center_id)
            self.user = user_center_member['user']
            self.center = user_center_member['center']
            self.center_member = user_center_member['center_member']

            self.center_reg_from = self.center_member['reg_from']
            self.center_reg_to = self.center_member['reg_to']
            self.last_visit_date = self.center_member['visit_date']

            report_set = WorkoutReportBuilder.build_date_period_workout_session_reports(user_id, from_date, to_date)
            if report_set : 
                total_volume = report_set.get_total_volume()
                total_workout_time = report_set.get_total_workout_time()
                workout_dhm = timedelta_to_dhm_format(total_workout_time)

            self.weekly_workout_summary = self.make_weekly_workout_summary(user_id, from_date, to_date)

    def make_weekly_workout_summary(self, user_id, from_date, to_date) : 
        total_volume = 0
        total_workout_time = timedelta()

        report_set = WorkoutReportBuilder.build_date_period_workout_session_reports(user_id, from_date, to_date)
        if report_set : 
            total_volume = report_set.get_total_volume()
            total_workout_time = report_set.get_total_workout_time()

        workout_dhm = timedelta_to_dhm_format(total_workout_time)
        return WeeklyWorkoutSummary(total_volume, workout_dhm)


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

