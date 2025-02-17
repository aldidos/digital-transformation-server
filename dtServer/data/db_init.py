import sys
sys.path.append('.')

import csv
from dtServer.data.conn import make_database_connection
from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.user_dao import userDao, User
from dtServer.data.dao.body_part_dao import bodyPartDao, BodyPart
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao, CenterEquipment
from dtServer.data.dao.center_dao import centerDao, Center
from dtServer.data.dao.center_member_dao import centerMemberDao, CenterMember
from dtServer.data.dao.center_staff_dao import centerStaffDao, CenterStaff
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao, ExerciseLibrary
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao, ExerciseLibBodyPart
from dtServer.data.dao.user_account_dao import userAccountDao, UserAccount
from dtServer.data.dao.user_center_dao import userCenterDao, UserCenter
from dtServer.data.dao.weight_metric_session_dao import weightMetricSession, WeightMetricSession
from dtServer.data.dao.weight_metric_dao import weightMetricDao, WeightMetric
from dtServer.data.dao.user_survey_dao import userSurveyDao, UserSurvey
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao, WorkoutSessions
from dtServer.data.dao.workouts_dao import workoutDao, Workouts
from dtServer.data.dao.workout_set_dao import workoutSetDao, WorkoutSet
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao, WorkoutMetrics
from dtServer.data.dao.nfc_tag_dao import nfcTagDao, NFCTag
from dtServer.data.dao.equipment_dao import equipmentDao, Equipment
from dtServer.data.dao.exercise_library_type_dao import exerciseLibraryTypeDao, ExerciseLibraryType
from dtServer.data.dao.exercise_library_difficulty_dao import exerciseLibraryDifficultyDao, ExerciseLibraryDifficulty
from dtServer.data.dao.user_fvp_profile_dao import userFVPProfileDao, UserFVPProfile
from dtServer.data.dao.user_fvp_profile_value_dao import userFVPProfileValueDao, UserFVPProfileValue
from dtServer.data.dao.workout_exerciselib_dao import workoutExerciselibDao, WorkoutExerciseLib
from dtServer.data.dao.workout_bodypart_dao import workoutBodypartDao, WorkoutBodypart

def open_data_file_csv(file_path : str) : 
     with open(file_path, 'r', encoding='utf-8') as f : 
        csv_reader = csv.DictReader(f)
        list_data = list(csv_reader)
        return list_data

def init_equipments() : 
    list_data = open_data_file_csv('./data/required_data/equipments.csv')
    equipmentDao.insert_many(list_data)

def init_bodyparts() : 
    list_data = open_data_file_csv('./data/required_data/body_parts.csv')
    bodyPartDao.insert_many(list_data)

def init_exerciselibraries() : 
    list_data = open_data_file_csv('./data/required_data/exercise_libraries.csv')
    exerciseLibraryDao.insert_many(list_data)

def init_exerciselibrary_bodypart() : 
    with open('./data/required_data/exerciselibrary_bodypart.txt', 'r', encoding='utf-8') as f : 
        csv_reader = csv.reader(f, delimiter='\t') 
        csv_reader.__next__()
        for row in csv_reader : 
            el_id = row[0]
            bp_id = row[1]  
            bp_ids = bp_id.split(',')
            for temp_bp_id in bp_ids : 
                exerciseLibBodyPartDao.insert(int(el_id), int(temp_bp_id))

def init_users() : 
    list_data = open_data_file_csv('./data/test_data/users.csv')
    userDao.insert_many(list_data)

def init_user_account() : 
    list_data = open_data_file_csv('./data/test_data/user_account.csv')
    userAccountDao.insert_many(list_data)

def init_center() : 
    list_data = open_data_file_csv('./data/test_data/center.csv')
    centerDao.insert_many(list_data)

def init_center_members() : 
    list_data = open_data_file_csv('./data/test_data/center_members.csv')
    centerMemberDao.insert_many(list_data)

def init_center_equipments() : 
    list_data = open_data_file_csv('./data/test_data/center_equipments.csv')
    centerEquipmentDao.insert_many(list_data)

def init_center_staffs() : 
    list_data = open_data_file_csv('./data/test_data/center_staffs.csv')
    centerStaffDao.insert_many(list_data)       

def init_user_center() : 
    list_data = open_data_file_csv('./data/test_data/user_center.csv')
    userCenterDao.insert_many(list_data) 

def init_workout_sessions() : 
    list_data = open_data_file_csv('./data/test_data/workout_session.csv')
    workoutSessionDao.insert_many(list_data)    

def init_workouts() : 
    list_data = open_data_file_csv('./data/test_data/workout.csv')
    workoutDao.insert_many(list_data)

def init_workout_sets() : 
    list_data = open_data_file_csv('./data/test_data/workout_sets.csv')
    workoutSetDao.insert_many(list_data)

def init_workout_metrics() : 
    workout_metrics = open_data_file_csv('./data/test_data/workout_metrics.csv')
    workoutMetricDao.insert_many(workout_metrics)    
    
def init_nfc_tags() : 
    list_data = open_data_file_csv('./data/test_data/nfc_tags.csv')
    nfcTagDao.insert_many(list_data)

def init_exercise_library_type() : 
    list_data = open_data_file_csv('./data/required_data/exercise_library_type.csv')
    exerciseLibraryTypeDao.insert_many(list_data)

def init_exercise_library_difficulty() : 
    list_data = open_data_file_csv('./data/required_data/exercise_library_difficulty.csv')
    exerciseLibraryDifficultyDao.insert_many(list_data)

def init_workout_exerciselib() : 
    list_data = open_data_file_csv('./data/test_data/workout_exerciselib.csv')
    workoutExerciselibDao.insert_many(list_data)    

def init_wokrout_bodypart() : 
    list_data = open_data_file_csv('./data/test_data/workout_bodypart.csv')
    workoutBodypartDao.insert_many(list_data)    


if __name__ == '__main__' : 
    tables = [
              User, WorkoutSessions, Workouts, Center, WorkoutMetrics, WorkoutSet, WorkoutExerciseLib, WorkoutBodypart, 
              BodyPart, CenterEquipment, CenterMember, CenterStaff, 
              ExerciseLibrary, ExerciseLibBodyPart, UserAccount, UserCenter, WeightMetricSession, 
              UserSurvey, NFCTag, Equipment, UserFVPProfile, UserFVPProfileValue, ExerciseLibraryType, ExerciseLibraryDifficulty
              ]
    
    conn = make_database_connection()   
    db_proxy.initialize(conn)

    conn.drop_tables( tables, safe = True)
    conn.create_tables( tables )    

    init_exercise_library_type()
    init_exercise_library_difficulty()
    init_bodyparts()
    init_equipments()
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
    init_workout_exerciselib()
    init_wokrout_bodypart()
    init_workout_sets()
    init_workout_metrics()

    init_nfc_tags()

    if not conn.is_closed() : 
        conn.close()
    