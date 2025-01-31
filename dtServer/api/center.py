from dtServer.data.model.center import save_center, select_center_by_id, select_center_by_name_address
from dtServer.data.model.center_member import save_center_member, select_center_members, select_center_member, select_center_member_by_id
from dtServer.data.model.center_staff import save_center_staff, select_center_staffs, select_center_staff
from dtServer.data.model.center_equipment import save_center_euipment, select_center_euipment, select_center_euipments
from dtServer.data.model.equipment import save_equipment, select_equipments
from dtServer.data.data_converter import model_to_dict_or_none

def post_center(data) : 
    return save_center(data)

def get_center_by_id(center_id : int) :     
    center = select_center_by_id(center_id) 
    return model_to_dict_or_none(center)

def get_center(center_name, address) : 
    center = select_center_by_name_address(center_name, address)
    return model_to_dict_or_none(center)

def post_center_member(data) : 
    return save_center_member(data)

def get_center_members(center_id : int) : 
    return select_center_members(center_id)

def get_center_member_by_id(center_id) : 
    center_member = select_center_member_by_id(center_id)
    return model_to_dict_or_none(center_member)

def put_center_member(data) :
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
    center_equipment = select_center_euipment(center_equipment_id)
    return model_to_dict_or_none(center_equipment)

def post_equipment(data) : ####
    return save_equipment(data)

def get_equipments() : ####
    return select_equipments()

def get_center_authentication(center_id, user_name, birthday, contact) :     
    center_member = select_center_member(center_id, user_name, birthday, contact)
    return model_to_dict_or_none(center_member)
