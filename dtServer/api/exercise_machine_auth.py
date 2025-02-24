from dtServer.app import scheduler

auth_keys = dict()

JOB_ID = f'machine_auth'
JOB_SECONDS = 180

def get_key_data(machine_key) : 
    return auth_keys.get(machine_key)    

def pop_key_data(machine_key) :     
    return auth_keys.pop(machine_key, None)

def remove_machine_auth_key(machine_key, job_id) :     
    scheduler.remove_job(job_id)
    print('DEBUG : remove_machine_auth_key')
    return pop_key_data(machine_key)

def add_machine_key_value(machine_key, data) : 
    auth_keys[machine_key] = data
    job_id = f'{JOB_ID}:{machine_key}'      
    scheduler.add_job(remove_machine_auth_key, 'interval', seconds=JOB_SECONDS, args=[machine_key, job_id], id = job_id)    
