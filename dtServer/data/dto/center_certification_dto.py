
class CenterCertificationDTO : 

    def __init__(self, data : dict) : 
        self.form = data

    def get_user_id(self) : 
           return self.form['user_id']
    
    def get_center_name(self) : 
           return self.form['center_name']
    
    def get_center_address(self) : 
           return self.form['center_address']
    
    def get_data(self) : 
          return self.form