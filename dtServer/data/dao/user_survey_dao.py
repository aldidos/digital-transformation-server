from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.user_survey import UserSurvey, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class UserSurveyDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(UserSurvey, data) )
    
    def select_by_user(self, user_id : int) :
        user_survey = UserSurvey.get_or_none(UserSurvey.user == user_id)
        return model_to_dict_or_none(user_survey)    

userSurveyDao = UserSurveyDao()