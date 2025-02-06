import sys
sys.path.append('.')
import csv

from dtServer.data.conn import make_database_connection
from dtServer.data.model.base_model import db_proxy
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
from dtServer.data.model.user_exercise_metric_value import UserExerciseMetricValue
from dtServer.data.model.user_survey import UserSurvey
from dtServer.data.model.workout_sessions import WorkoutSessions, insert_workout_sessions
from dtServer.data.model.workouts import Workouts, insert_workouts
from dtServer.data.model.workout_metrics import WorkoutMetrics, insert_many_workout_metrics
from dtServer.data.model.user_fvp_profile import UserFVPProfile
from dtServer.data.model.user_fvp_profile_value import UserFVPProfileValue
from dtServer.data.model.nfc_tag import NFCTag, insert_nfc_tags
from dtServer.data.model.exercise_library_equipment import ExerciseLibraryEquipment, insert_exerciselibrary_equipments
from dtServer.data.model.exercise_library_type import ExerciseLibraryType, insert_many_exercise_library_type
from dtServer.data.model.exercise_library_difficulty import ExerciseLibraryDifficulty, insert_many_exercise_library_difficulty

def open_data_file_csv(file_path : str) : 
     with open(file_path, 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        return list_data

def init_exerciselibrary_equipments() : 
    list_data = open_data_file_csv('./data/required_data/exerciselibrary_equipments.csv')
    insert_exerciselibrary_equipments(list_data)

def init_bodyparts() : 
    list_data = open_data_file_csv('./data/required_data/body_parts.csv')
    insert_body_parts(list_data)

def init_exerciselibraries() : 
    list_data = open_data_file_csv('./data/required_data/exercise_libraries.csv')
    insert_many_exercise_libraries(list_data)

def init_exerciselibrary_bodypart() : 
    with open('./data/required_data/exerciselibrary_bodypart.txt', 'r', encoding='utf-8') as f : 
        csv_reader = csv.reader(f, delimiter='\t') 
        csv_reader.__next__()
        for row in csv_reader : 
            el_id = row[0]
            bp_id = row[1]  
            bp_ids = bp_id.split(',')
            for temp_bp_id in bp_ids : 
                insert_exerciselibrary_body_part(int(el_id), int(temp_bp_id))

def init_users() : 
    list_data = open_data_file_csv('./data/test_data/users.csv')
    insert_users(list_data)

def init_user_account() : 
    list_data = open_data_file_csv('./data/test_data/user_account.csv')
    insert_user_accounts(list_data)

def init_center() : 
    list_data = open_data_file_csv('./data/test_data/center.csv')
    insert_centers(list_data)

def init_center_members() : 
    list_data = open_data_file_csv('./data/test_data/center_members.csv')
    insert_center_members(list_data)

def init_center_equipments() : 
    list_data = open_data_file_csv('./data/test_data/center_equipments.csv')
    insert_center_equipments(list_data)

def init_center_staffs() : 
    list_data = open_data_file_csv('./data/test_data/center_staffs.csv')
    insert_center_staffs(list_data)

def init_user_center() : 
    list_data = open_data_file_csv('./data/test_data/user_center.csv')
    insert_user_center(list_data) 

def init_workout_sessions() : 
    list_data = open_data_file_csv('./data/test_data/workout_session.csv')
    insert_workout_sessions(list_data)

def init_workouts() : 
    list_data = open_data_file_csv('./data/test_data/workout.csv')
    insert_workouts(list_data)

def init_workout_metrics() : 
    list_data = open_data_file_csv('./data/test_data/workout_metrics.csv')
    insert_many_workout_metrics(list_data)

def init_nfc_tags() : 
    list_data = open_data_file_csv('./data/test_data/nfc_tags.csv')
    insert_nfc_tags(list_data)

def init_exercise_library_type() : 
    list_data = open_data_file_csv('./data/required_data/exercise_library_type.csv')
    insert_many_exercise_library_type(list_data)

def init_exercise_library_difficulty() : 
    list_data = open_data_file_csv('./data/required_data/exercise_library_difficulty.csv')
    insert_many_exercise_library_difficulty(list_data)

if __name__ == '__main__' : 
    tables = [
              User, WorkoutSessions, Workouts, Center, WorkoutMetrics,  
              BodyPart, CenterEquipment, CenterMember, CenterStaff, EquipmentExerciseLib, 
              ExerciseLibrary, ExerciseLibBodyPart, UserAccount, UserCenter, UserExerciseMetric, UserExerciseMetricValue, 
              UserSurvey, NFCTag, ExerciseLibraryEquipment, UserFVPProfile, UserFVPProfileValue, ExerciseLibraryType, ExerciseLibraryDifficulty
              ]
    
    conn = make_database_connection()   
    db_proxy.initialize(conn)

    conn.drop_tables( tables, safe = True)
    conn.create_tables( tables )    

    init_exercise_library_type()
    init_exercise_library_difficulty()
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
    init_workout_metrics()

    init_nfc_tags()

    if not conn.is_closed() : 
        conn.close()
    