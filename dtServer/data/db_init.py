import sys
sys.path.append('.')
import csv

from dtServer.data.conn import make_database_connection
from dtServer.data.model.base_model import db_proxy
from dtServer.data.model.equipment import Equipment
from dtServer.data.model.user import User
from dtServer.data.model.body_part import BodyPart, insert_body_parts
from dtServer.data.model.center_equipment import CenterEquipment
from dtServer.data.model.center import Center
from dtServer.data.model.center_member import CenterMember
from dtServer.data.model.center_staff import CenterStaff
from dtServer.data.model.equipment_exerciselib import EquipmentExerciseLib
from dtServer.data.model.exercise_library import ExerciseLibrary, insert_many_exercise_libraries
from dtServer.data.model.exerciselib_bodypart import ExerciseLibBodyPart, insert_exerciselibrary_body_part
from dtServer.data.model.user_account import UserAccount
from dtServer.data.model.user_center import UserCenter
from dtServer.data.model.user_exercise_metric import UserExerciseMetric
from dtServer.data.model.user_survey import UserSurvey
from dtServer.data.model.workout_sessions import WorkoutSessions
from dtServer.data.model.workouts import Workouts
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.model.nfc_tag import NFCTag
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

if __name__ == '__main__' :     
    tables = [ User, Equipment, WorkoutSessions, Workouts, Center, WorkoutMetrics, 
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

    if not conn.is_closed() : 
        conn.close()
    