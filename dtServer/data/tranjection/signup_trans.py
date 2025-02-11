from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.user_account_dao import userAccountDao

class SignupTrans : 

    def insert_signup_data(self, user_info, user_account) : 
        with db_proxy.atomic() : 
            user = userDao.save(user_info)
            user_account['user_id'] = user['id']
            userAccountDao.save(user_account)
            return user
        
signupTrans = SignupTrans()