import sys
sys.path.append('.')
import csv

from dtServer.data.conn import make_database_connection
from dtServer.data.model.base_model import db_proxy
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.user import User, insert_users
from dtServer.data.model.body_part import BodyPart, insert_body_parts
from dtServer.data.model.center_equipment import CenterEquipment, insert_center_equipments
from dtServer.data.model.center import Center, insert_centers
from dtServer.data.model.center_member import CenterMember, insert_center_members
from dtServer.data.model.center_staff import CenterStaff, insert_center_staffs
from dtServer.data.model.equipment_exerciselib import EquipmentExerciseLib
from dtServer.data.model.exercise_library import ExerciseLibrary, insert_many_exercise_libraries
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart, insert_exerciselibrary_body_part
from dtServer.data.model.user_account import UserAccount, insert_user_accounts
from dtServer.data.model.user_center import UserCenter, insert_user_center
from dtServer.data.model.user_exercise_metric import UserExerciseMetric
from dtServer.data.model.user_survey import UserSurvey
from dtServer.data.model.workout_sessions import WorkoutSessions, insert_workout_sessions
from dtServer.data.model.workouts import Workouts, insert_workouts
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.model.nfc_tag import NFCTag, insert_nfc_tags
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment, insert_exerciselibrary_equipments

def init_exerciselibrary_equipments() : 
    with open('./data/exerciselibrary_equipments.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_exerciselibrary_equipments(list_data)

def init_bodyparts() : 
    with open('./data/body_parts.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_body_parts(list_data)

def init_exerciselibraries() : 
    with open('./data/exercise_libraries.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_many_exercise_libraries(list_data)

def init_exerciselibrary_bodypart() : 
    with open('./data/exerciselibrary_bodypart.txt', 'r', encoding='utf-8') as f : 
        csv_reader = csv.reader(f, delimiter='\t') 
        csv_reader.__next__()
        for row in csv_reader : 
            el_id = row[0]
            bp_id = row[1]  
            bp_ids = bp_id.split(',')
            for temp_bp_id in bp_ids : 
                insert_exerciselibrary_body_part(int(el_id), int(temp_bp_id))

def init_users() : 
    with open('./data/users.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_users(list_data)

def init_user_account() : 
    with open('./data/user_account.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_user_accounts(list_data)

def init_center() : 
    with open('./data/center.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_centers(list_data)

def init_center_members() : 
    with open('./data/center_members.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_center_members(list_data)

def init_center_equipments() : 
    with open('./data/center_equipments.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_center_equipments(list_data)

def init_center_staffs() : 
    with open('./data/center_staffs.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_center_staffs(list_data) 

def init_user_center() : 
    with open('./data/user_center.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_user_center(list_data)    

def init_workout_sessions() : 
    with open('./data/workout_session.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_workout_sessions(list_data)

def init_workouts() : 
    with open('./data/workout.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_workouts(list_data)  

def init_nfc_tags() : 
    with open('./data/nfc_tags.csv', 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        insert_nfc_tags(list_data)  

if __name__ == '__main__' : 
    tables = [User, Equipment, WorkoutSessions, Workouts, Center, WorkoutMetrics, 
              BodyPart, CenterEquipment, CenterMember, CenterStaff, EquipmentExerciseLib, 
              ExerciseLibrary, ExerciseLibBodyPart, UserAccount, UserCenter, UserExerciseMetric, 
              UserSurvey, NFCTag, ExerciseLibraryEquipment
              ]
    
    conn = make_database_connection()   
    db_proxy.initialize(conn)

    conn.drop_tables( tables, safe = True)
    conn.create_tables( tables )    

    init_bodyparts()
    init_exerciselibrary_equipments()
    init_exerciselibraries()
    init_exerciselibrary_bodypart()

    init_users()
    init_user_account()
    init_center()
    init_center_members()

    init_center_equipments()
    init_center_staffs()
    init_user_center()
    init_workout_sessions()
    init_workouts()
    init_nfc_tags()

    if not conn.is_closed() : 
        conn.close()
    