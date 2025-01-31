from dtServer.data.model.user import save_user, select_user_by_id
from dtServer.data.model.user_account import save_user_account, get_user_account_by_loginid
from dtServer.data.model.user_survey import save_user_survey, select_user_survey
from dtServer.data.data_converter import model_to_dict_or_none

def signup_user(user_account, user_info) : 
    login_id = user_account['login_id']
    prev_user_account = model_to_dict_or_none( get_user_account_by_loginid(login_id) )

    if prev_user_account == None : 
        user = save_user(user_info)
        user_account['user_id'] = user['id']
        save_user_account(user_account) 
        return user
    else : 
        return None

def singin_user(login_id) : 
    user_account = get_user_account_by_loginid(login_id)
    return model_to_dict_or_none(user_account)

def get_user(user_id) : 
    user = select_user_by_id(user_id)
    return model_to_dict_or_none(user)

def post_user_survey(data) : 
    return save_user_survey(data)

def get_user_survey(user_id) : 
    user_survey = select_user_survey(user_id)    
    return model_to_dict_or_none(user_survey)