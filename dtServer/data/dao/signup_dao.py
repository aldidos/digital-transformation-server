from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.dao.user_account_dao import userAccountDao, db_proxy, model_to_dict_or_none
from dtServer.data.dao.user_dao import userDao
from playhouse.shortcuts import model_to_dict, dict_to_model

class SignupDao(BaseDAO) :     

    def insert_signup_data(self, user_info, user_account) : 
        with db_proxy.atomic() : 
            user = userDao.save(user_info)
            user_account['user_id'] = user['id']
            userAccountDao.save(user_account)
            return user

signupDao = SignupDao()