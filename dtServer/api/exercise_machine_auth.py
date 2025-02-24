
auth_keys = dict()

def get_key_data(machine_key) : 
    return auth_keys.get(machine_key)    

def pop_key_data(machine_key) : 
    return auth_keys.pop(machine_key, None)    

def add_machine_key_value(machine_key, data) : 
    auth_keys[machine_key] = data
