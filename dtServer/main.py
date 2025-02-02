import sys
sys.path.append('./')
from flask import Flask, request, session, abort
from dtServer.data.conn import make_database_connection, db_proxy
import datetime
from dtServer.data.model.user_center import get_user_centers, create_user_center, get_user_center
from dtServer.data.model.user import save_user, select_user_by_id
from dtServer.data.model.user_account import get_user_account_by_loginid, save_user_account
from dtServer.data.model.center import get_center_by_name_address, save_center, get_center_by_id
from dtServer.data.model.center_member import get_center_member, save_center_member, select_center_members, select_center_member_by_id
from dtServer.data.model.center_staff import save_center_staff, select_center_staffs
from dtServer.data.model.center_equipment import select_center_euipments
from dtServer.data.model.exercise_library import select_exericse_libraries
from dtServer.data.model.user_exercise_metric import save_user_exercise_metric, select_user_exer_metric
from dtServer.data.model.user_survey import save_user_survey, select_user_survey
from dtServer.data.model.workout_sessions import save_workout_session, select_workout_sessions_period, select_workout_sessions
from dtServer.data.model.workouts import save_workout, select_workouts, select_workout_by_id
from dtServer.data.model.workout_metrics import insert_multiple_workout_metrics, select_join_with_workout_sessions
from dtServer.data.model.nfc_tag import select_nfc_tag

app = Flask(__name__)
app.secret_key = b'_@sD2&f^L(i8p]2#mHzVs1@^&gj]'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=5)

db_conn = make_database_connection()
db_proxy.initialize(db_conn)

@app.before_request
def connect_db() : 
     global db_conn
     if db_conn.is_closed() : 
          db_conn = make_database_connection() 

@app.teardown_request
def close_db_conn(exc) : 
     global db_conn     
     if not db_conn.is_closed() : 
          db_conn.close()

@app.errorhandler(400)
def request_error_bad_request(e) : 
     return "Bad request", 400

@app.errorhandler(404)
def request_error_not_found(e) : 
     return "Resource not found", 404

@app.route("/signup", methods = ['POST'])
def signup() :
    if request.method == 'POST' : 
          data = request.get_json()
          user_account = data['user_account']
          user_info = data['user_info'] 

          login_id = user_account['login_id']
          prev_user_account = get_user_account_by_loginid(login_id)

          if prev_user_account == None : 
               user = save_user(user_info)
               user_account['user_id'] = user['id']
               save_user_account(user_account)
               return (user, 200)
          else : 
               return abort(400)

@app.route("/signin", methods=['GET']) 
def signin() : 
     data = request.get_json()
     login_id = data['login_id']
     login_pw = data['login_pw']     

     user_account = get_user_account_by_loginid(login_id)

     if user_account is None : 
        return abort(400)
     
     if login_pw == user_account['login_pw'] : 
          return (user_account['user_id'], 200) 
     return abort(400)

@app.route("/centers/authentication", methods=['POST', 'GET'])
def center_authentication() : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_name = data['center_name']
          center_address = data['center_address']
          user_id = data['user_id']
          user_name = data['user_name']
          birthday = data['birthday']
          contact = data['contact'] 

          center = get_center_by_name_address(center_name, center_address)
          if center is not None : 
               center_id = center['id']

               user_center = get_user_center(user_id, center_id)
               if user_center is None : 
                    return ("the center authentication has been done", 400)

               center_member = get_center_member(center_id, user_name, birthday, contact)
               if center_member is not None : 
                    create_user_center(user_id, center_id)
                    return (center_member, 200)
               return ("Center authentication faild", 400)
          
          return ("Center authentication faild", 400)
     
     if request.method == 'GET' : 
          data = request.get_json()
          user_id = data['user_id']
          user_centers = get_user_centers(user_id)
          if not user_centers : 
               return abort(404) ## user's center authentication cannot found.
          return (user_centers, 200)

@app.route("/centers", methods=['POST'])
def centers() : 
     data = request.get_json()
     center = save_center(data)
     if center is None :
          return abort(400)
     return (center, 201)

@app.route("/centers/<center_id>", methods=['GET'])
def center(center_id : int) : 
     center = get_center_by_id(center_id) 
     if center is None : 
          return abort(400)
     return (center, 200)

@app.route("/centers/<center_id>/members", methods=['GET', 'POST'])
def center_members(center_id : int) :
     if request.method == 'POST' : 
          data = request.get_json()
          center_member = save_center_member(data)          
          if center_member is None :
               return abort(400)
          return (center_member, 200)
               
     if request.method == 'GET' : 
          center_members = select_center_members(center_id) 
          return (center_members, 200)

@app.route("/centers/<center_id>/members/<member_id>", methods=['GET', 'PUT'])
def get_put_center_member(center_id, member_id) : 
     if request.method == 'GET' : 
          center_member = select_center_member_by_id(member_id)
          if center_member is None : 
               return ("Resource not found", 400)
          return (center_member, 200)
     
     if request.method == 'PUT' : 
          data = request.get_json()
          save_center_member(data)
          return ("put a center member", 200) 
     
@app.route("/centers/<center_id>/staffs", methods=['GET', 'POST'])
def center_staffs(center_id : int) : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_staff = save_center_staff(data)
          if center_staff is None :
               return abort(400) 
          return (center_staff, 200)
     
     if request.method == 'GET' : 
          center_staffs = select_center_staffs(center_id)  ####
          return (center_staffs, 200)

@app.route("/centers/<center_id>/equipments", methods=['GET'])
def center_equipments(center_id) : 
     if request.method == 'GET' : 
          center_equipments = select_center_euipments(center_id) ####
          return (center_equipments, 200) 

@app.route("/exercise_libraries", methods=['GET'])
def get_req_exercise_libraries() : 
     if request.method == 'GET' : 
          exercise_libs = select_exericse_libraries() 
          return (exercise_libs, 200)

@app.route("/users/<user_id>/weight_metric/<exercise_lib_id>", methods=['POST']) 
def post_req_user_exercise_metric(user_id, exercise_lib_id):
     if request.method == 'POST' : 
          data = request.get_json()
          user_exercise_weight = save_user_exercise_metric(data)
          return (user_exercise_weight, 200)

@app.route("/users/<user_id>/weight_metric/<exercise_lib_id>", methods=['GET', 'PATCH']) 
def get_patch_req_user_exercise_metric(user_id, exercise_lib_id) :
     if request.method == 'GET' : 
          user_weight_metric = select_user_exer_metric(user_id, exercise_lib_id)
          if user_weight_metric is None : 
               return abort(404)               
          return (user_weight_metric, 200)
     
     if request.method == 'PATCH' : 
          data = request.get_json()
          save_user_exercise_metric(data)
          return ("PATCH the user exercise weight metric", 200)

@app.route("/users/<user_id>/survey", methods=['GET', 'POST', 'PATCH']) 
def users_survey(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          user_survey = save_user_survey(data) 
          if user_survey is None : 
               return abort(400)               
          return (user_survey, 200) 

     if request.method == 'GET' : 
          user_survey = select_user_survey(user_id)
          if user_survey is None : 
               return abort(404)  
          return (user_survey, 200)
     
     if request.method == 'PATCH' : 
          data = request.get_json()
          user_survey = save_user_survey(data) 
          return ('PATCH requested user survey', 200)

@app.route("/users/<user_id>", methods=['GET'])
def get_req_users(user_id):
     user = select_user_by_id(user_id)     
     if user is None : 
          return abort(400)
     return (user, 200)

@app.route("/users/<user_id>/workout_history/workout_sessions", methods=['GET', 'POST', 'PATCH'])  ####
def get_post_patch_req_user_workout_sessions(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()          
          user_workout_session = save_workout_session(data)
          return (user_workout_session, 201)
          
     if request.method == 'GET' : 
          type = request.args.get('search_type')
          if type == 'period' : 
               from_date = request.args.get('from_date')
               to_date = request.args.get('to_date')          
               user_workout_sessions = select_workout_sessions_period(user_id, from_date, to_date)               
          else : 
               date = request.args.get('date')
               user_workout_sessions = select_workout_sessions(user_id, date)
               
          return (user_workout_sessions, 200)
     
     if request.method == 'PATCH' : 
          data = request.get_json()
          save_workout_session(data)
          return ("patched user workout session", 200)

@app.route("/users/<user_id>/workout_history/<workout_session_id>/workouts", methods=['GET', 'POST']) 
def get_post_req_workouts(user_id, workout_session_id) : 
     if request.method == "POST" : 
          data = request.get_json()          
          save_workout(data)          
          return ("POSTED user workout data", 200)
     
     if request.method == "GET" :           
          workouts = select_workouts(workout_session_id) 
          return (workouts, 200)

@app.route("/users/<user_id>/workout_history/<workout_session_id>/<workout_id>", methods=['GET', 'PATCH']) 
def get_put_workout(user_id, workout_session_id, workout_id) :      
     if request.method == "PATCH" : ####
          data = request.get_json()
          if save_workout(data) : 
               return ("PATCH workout data", 200)
          return ("FAILD : patch workout data", 400) 
     
     if request.method == "GET" :           
          workout = select_workout_by_id(workout_id)
          if workout is None : 
               return abort(400)
          return (workout, 200)

@app.route("/users/<user_id>/workout_metrics", methods=['GET', 'POST']) 
def post_get_req_workout_metrics(user_id) : 
     if request.method == "POST" : 
          list_data = request.get_json()
          insert_multiple_workout_metrics( list_data )
          return ("post workout metrcis", 200)
     
     if request.method == "GET" : 
          from_date = request.args.get('from_date') 
          to_date = request.args.get('to_date') 

          workout_metrics = select_join_with_workout_sessions(user_id, from_date, to_date)
          return (workout_metrics, 200)

@app.route("/nfc_certification", methods=['POST', "GET"]) ####
def nfc_certification() : 
     if request.method == 'POST' :
          data = request.get_json()
          nfc_tag_id = data['nfc_tag_id']
          user_id = data['user_id']

          nfc_tag = select_nfc_tag(nfc_tag_id)
          if nfc_tag is None : 
               return abort(400)
          else :                
               session['nfc_tag_certification'] = {
                    'nfc_tag_id' : nfc_tag_id, 
                    'user_id' : user_id
               }
               return ("created nfc certification session", 200) 
          
     if request.method == 'GET' : 
          if 'nfc_tag_certification' in session : 
               return ( session['nfc_tag_certification'], 200)
          
          return abort(400)

@app.route("/qr_certification", methods=['POST', 'GET']) ####
def qr_certification() : 
     data = request.get_json()
     if request.method == 'POST' :           
          session['qr_certification'] = data

          return ("QR certification ready", 200)
     if request.method == 'GET' :           
          if 'qr_certification' in session : 
               certification_data = session['qr_certification']
               return (certification_data, 200)          
          return abort(400)

@app.route("/users/<user_id>/workouts_report", methods=['GET']) ####
def get_workout_metrics_by_exercise_libs(user_id) : 
     pass 
