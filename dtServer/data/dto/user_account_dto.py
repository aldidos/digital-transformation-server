
class UserAccountDTO : 

    def __init__(self, user_account : dict) : 
        self.user_account = user_account

    def get_login_id(self) : 
        return self.user_account['login_id']

    def get_login_pw(self) : 
        return self.user_account['login_pw']
    
    def get_user_account(self) : 
        return self.user_account

    def valid_user_account(self) : 
        login_id = self.user_account['login_id']
        login_pw = self.user_account['login_pw']
        if len(login_id) < 4 : 
            return 'THIS MESSGAE IS SENT DURING DEVELOPING : the length of login_id must be over 4', False
        if len(login_pw) < 4 : 
            return 'THIS MESSGAE IS SENT DURING DEVELOPING : the length of login_pw must be over 4', False

        return 'THIS MESSGAE IS SENT DURING DEVELOPING : the login id and pw can be used', True        