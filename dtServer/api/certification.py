from dtServer.api.user import get_user
from dtServer.api.center import get_center_equipment
from dtServer.data.model.nfc_tag import select_nfc_tag, save_nfc_tag

def put_nfc_access(data) :
    save_nfc_tag(data)

def get_nfc_tag(nfc_tag_id, user_id, center_equipment_id) : ####
    model = select_nfc_tag(nfc_tag_id, user_id, center_equipment_id)
    return model

def get_qr_certification(user_id, center_equipment_id) : ####
    user = get_user(user_id)
    if user is None : 
        return None    
    
    center_equipment = get_center_equipment(center_equipment_id)    
    return { 'user' : user, 'center_equipment' : center_equipment }
    