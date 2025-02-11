
class MachineCertificationForm : 

    def __init__(self, data : dict) : 
        self.form = data

    def get_nfc_tag_id(self) : 
           return self.form['nfc_tag_id']
    
    def get_user_id(self) : 
           return self.form['user_id']
    
    def get_center_equipment_id(self) : 
           return self.form['center_equipment_id']
    
    def get_workout_session_id(self) : 
           return self.form['workout_session_id']
    
    def get_data(self) : 
          return self.form