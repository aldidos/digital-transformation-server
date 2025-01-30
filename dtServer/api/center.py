from dtServer.data.model.center import save_center, select_center_by_id, select_center_by_name_address
from dtServer.data.model.center_member import save_center_member, select_center_members, select_center_member, select_center_member_by_id
from dtServer.data.model.center_staff import save_center_staff, select_center_staffs, select_center_staff
from dtServer.data.model.center_equipment import save_center_euipment, select_center_euipment, select_center_euipments
from dtServer.data.model.equipment import save_equipment, select_equipments

def post_center(data) : 
    return save_center(data)

def get_center_by_id(center_id : int) :     
    center = select_center_by_id(center_id) 
    return center

def get_center(center_name, address) : 
    center = select_center_by_name_address(center_name, address)
    return center

def post_center_member(data) : 
    return save_center_member(data)

def get_center_members(center_id : int) : 
    return select_center_members(center_id)

def get_center_member_by_id(center_id) : 
    return select_center_member_by_id(center_id)

def put_center_member(center_member_id, data) :
    data['id'] = center_member_id
    return save_center_member(data)

def post_center_staff(data) : 
    return save_center_staff(data)

def get_center_staffs(center_id : int) : 
    return select_center_staffs(center_id)

def post_center_equipment(data) : 
    return save_center_euipment(data)

def get_center_equipments(center_id : int) : 
    return select_center_euipments(center_id)

def get_center_equipment(center_equipment_id : int) : 
    return select_center_euipment(center_equipment_id)

def post_equipment(data) : 
    n = save_equipment(data)
    if n > 0 : 
        return True
    return False

def get_equipments() : 
    return select_equipments()

def get_center_authentication(center_id, user_name, birthday, contact) :     
    center_member = select_center_member(center_id, user_name, birthday, contact)
    return center_member
