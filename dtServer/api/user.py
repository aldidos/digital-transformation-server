from dtServer.data.model.user import save_user, select_user_by_id
from dtServer.data.model.user_account import save_user_account, get_user_account_by_loginid
from dtServer.data.model.user_survey import save_user_survey, select_user_survey

def signup_user(user_account, user_info) : 
    login_id = user_account['login_id']
    if get_user_account_by_loginid(login_id) == None : 
        user = save_user(user_info)
        user_account['user_id'] = user.id
        save_user_account(user_account) 
        return user
    else : 
        return None

def singin_user(login_id) : 
    user_account = get_user_account_by_loginid(login_id)
    return user_account

def get_user(user_id) : 
    return select_user_by_id(user_id)

def post_user_survey(data) : 
    return save_user_survey(data)

def get_user_survey(user_id) : 
    return select_user_survey(user_id)    