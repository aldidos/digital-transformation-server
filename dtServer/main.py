import sys
sys.path.append('./')
from flask import Flask, request, session
from dtServer.data.conn import make_database_connection, db_proxy
from dtServer.api.user import signup_user, singin_user, post_user_survey, get_user_survey, get_user
from dtServer.api.center import post_center, get_center, get_center_by_id, post_center_member, get_center_members, post_center_staff, get_center_staffs, \
                                   post_center_equipment, get_center_equipment, get_center_equipments, post_equipment, get_equipments, get_center_authentication, \
                                   get_center_member_by_id, put_center_member
from dtServer.api.workout import get_exercise_libraries, post_exercise_library, post_user_weight_metric, get_user_weight_metric, patch_user_weight_metric, \
                                   post_user_workout_session, get_user_workout_sessions, patch_user_workout_session, get_user_workout_sessions_period, post_workout, \
                                   get_workouts, put_workout, get_workout, post_workout_metric, get_workout_metrics, patch_workout, post_workout_metrics
import datetime
import json
from dtServer.api.certification import get_qr_certification, get_nfc_tag

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
def request_error_bad_request() : 
     pass

@app.errorhandler(404) # 
def request_error_not_found() : 
     pass

@app.route("/", methods=['GET'])
def hello_world() : 
     return ("hello world", 200)

@app.route("/signup", methods = ['POST'])
def signup() :
    if request.method == 'POST' : 
           data = request.get_json()
           user_account = data['user_account']
           user_info = data['user_info'] 

           user = signup_user(user_account, user_info)
           if user is None : 
                ("", 400) 
           return (user, 200)

@app.route("/signin", methods=['GET']) 
def signin() : 
     data = request.get_json()
     login_id = data['login_id']
     login_pw = data['login_pw']

     user_account = singin_user(login_id)

     if user_account is None : 
        return ("wrong id or pw", 400)
     else :         
          if login_pw == user_account['login_pw'] : 
               return (user_account['user_id'], 200)
          else : 
               return ("wrong id or pw", 400)

@app.route("/centers/authentication", methods=['GET'])
def center_authentication() : 
     data = request.get_json()
     center_name = data['center_name']
     center_address = data['center_address']
     user_name = data['user_name']
     birthday = data['birthday']
     contact = data['contact'] 

     center = get_center(center_name, center_address)
     if center is not None : 
          center_id = center['id']
          center_member = get_center_authentication(center_id, user_name, birthday, contact)
          if center_member is not None : 
               return (center_member, 200)
          else :
               return ("Center authentication faild", 400)
     else : 
          return ("Center authentication faild", 400)

@app.route("/centers", methods=['POST'])
def centers() : 
     data = request.get_json()
     if post_center(data) :
          return ("POST a new center", 200) 
     else :
          return ("Faild : post a new center", 400)

@app.route("/centers/<center_id>", methods=['GET'])
def center(center_id : int) : 
     center = get_center_by_id(center_id) 
     if center is None : 
          return ("Wrong request", 400)
     else : 
          return (center, 200)

@app.route("/centers/<center_id>/members", methods=['GET', 'POST'])
def center_members(center_id : int) :
     if request.method == 'POST' : 
          data = request.get_json()
          
          if post_center_member(data) : 
               return ("post a center member", 200)
          else : 
               return ("Failed : post a center member", 400) 
     if request.method == 'GET' : 
          center_members = get_center_members(center_id) ####          
          return (center_members, 200)

@app.route("/centers/<center_id>/members<center_member_id>", methods=['GET', 'PUT'])
def get_put_center_member(center_id, center_member_id) : 
     if request.method == 'GET' : 
          center_member = get_center_member_by_id(center_member_id)
          if center_member is None : 
               return ("Resource not found", 400)
          return (center_member, 200)
     
     if request.method == 'PUT' : 
          data = request.get_json()
          if put_center_member(data) :
               return ("put a center member", 200)
          else : 
               return ("Failed : put a center member", 400)

@app.route("/centers/<center_id>/staffs", methods=['GET', 'POST'])
def center_staffs(center_id : int) : 
     if request.method == 'POST' : 
          data = request.get_json()

          if post_center_staff(data) :
               return ("post a center staff", 200)
          else :
               return ("FAILED : post a center staff", 400)  
     
     if request.method == 'GET' : 
          center_staffs = get_center_staffs(center_id)  ####
          return (center_staffs, 200)

@app.route("/centers/<center_id>/equipments", methods=['GET', 'POST'])
def center_equipments(center_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          if post_center_equipment(data) : 
               return ("Post a center equipment", 200)
          else : 
               return ("FAILD : Post a center equipment", 400)
     elif request.method == 'GET' : 
          center_equipments = get_center_equipments(center_id) ####
          return (center_equipments, 200) 

# @app.route("/equipments", methods=['GET', 'POST'])
# def equipments() : 
#      if request.method == 'POST' : 
#           data = request.get_json()
#           if post_equipment(data) : 
#                return ("", 200)
#           else :
#                return ("", 400) 

#      elif request.method == 'GET' : 
#           equipments = get_equipments()
#           return (equipments, 200)

@app.route("/exercise_libraries", methods=['GET'])
def exercise_libraries() :          
     if request.method == 'GET' : 
          exercise_libs = get_exercise_libraries() 
          return (exercise_libs, 200)

@app.route("/users/<user_id>/weight_metric/<exercise_lib_id>", methods=['POST']) ####
def post_user_weight_metric(user_id, exercise_lib_id):
     if request.method == 'POST' : 
          data = request.get_json()
          weight = data['weight_metric']
          if  post_user_weight_metric(user_id, exercise_lib_id, weight): 
               return ("", 200)
          else :
               return ("", 400)

@app.route("/users/<user_id>/weight_metric/<exercise_lib_id>", methods=['GET', 'PATCH']) ####
def user_weight_metric(user_id, exercise_lib_id) : 
     if request.method == 'GET' : 
          user_weight_metric = get_user_weight_metric(user_id, exercise_lib_id)
          if user_weight_metric is not None : 
               return (user_weight_metric, 200)
          else : 
               return ("", 404)
     
     elif request.method == 'PATCH' : 
          data = request.get_json()
          patch_user_weight_metric(data)
          return ("", 200)

@app.route("/users/<user_id>/survey", methods=['GET', 'POST']) 
def users_survey(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          if post_user_survey(data) : 
               return ("POST sent user survey", 200)
          else : 
               return ("FAILD : POST sent user survey", 400)

     if request.method == 'GET' : 
          user_survey = get_user_survey(user_id)
          return (user_survey, 200)

@app.route("/users/<user_id>", methods=['GET'])
def users(user_id):
     user = get_user(user_id)     
     if user is None : 
          return ("The user resource not exist", 400)
     return (user, 200)

@app.route("/users/<user_id>/workout_history/workout_sessions", methods=['GET', 'POST', 'PATCH'])  ####
def user_workout_sessions(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          date = data['date'] 
          status = data['status']
          user_workout_session = post_user_workout_session(user_id, date, status)
          return (user_workout_session, 200)
          
     if request.method == 'GET' : 
          type = request.args.get('search_type')
          if type == 'period' : 
               from_date = request.args.get('from_date')
               to_date = request.args.get('to_date')          
               user_workout_sessions = get_user_workout_sessions_period(user_id, from_date, to_date)               
          else : 
               date = request.args.get('date')
               user_workout_sessions = get_user_workout_sessions(user_id, date)
               
          return (user_workout_sessions, 200)
     
     if request.method == 'PATCH' : 
          data = request.get_json()
          patch_user_workout_session(data)
          return ("", 200)

@app.route("/users/<user_id>/workout_history/<workout_session_id>/workouts", methods=['GET', 'POST']) 
def get_post_workouts(user_id, workout_session_id) : 
     if request.method == "POST" :  ####
          data = request.get_json()
          workout = post_workout(data)
          if workout is None : 
               return ("FAILD : post workout", 400)
          return (workout, 200)
     
     if request.method == "GET" :           
          workouts = get_workouts(workout_session_id) ####
          return (workouts, 200)

@app.route("/users/<user_id>/workout_history/<workout_session_id>/<workout_id>", methods=['GET', 'PATCH']) 
def get_put_workout(user_id, workout_session_id, workout_id) :      
     if request.method == "PATCH" : ####
          data = request.get_json()
          if patch_workout(data) : 
               return ("PATCH workout data", 200)
          return ("FAILD : patch workout data", 400)          
     
     if request.method == "GET" :           
          workout = get_workout(workout_id)
          if workout is None : 
               return ("FAILD : get workout data", 400)          
          return (workout, 200)

@app.route("/users/<user_id>/workout_metrics", methods=['GET', 'POST']) ##
def post_get_workout_metrics(user_id) : 
     if request.method == "POST" : 
          list_data = request.get_json()
          post_workout_metrics( list_data )
          return ("post workout metrcis", 200)
     
     if request.method == "GET" : 
          from_date = request.args.get('from_date') 
          to_date = request.args.get('to_date') 

          workout_metrics = get_workout_metrics(user_id, from_date, to_date)
          return (workout_metrics, 200)

@app.route("/nfc_certification", methods=['PUT', "GET"]) ####
def nfc_certification() : 
     if request.method == 'PUT' :  
          data = request.get_json()
          nfc_tag_id = data['nfc_tag_id']

          nfc_tag = get_nfc_tag(nfc_tag_id)
          if nfc_tag is None : 
               return ("Wrong TAG ID", 400)
          else : 
               session['nfc_tag_key'] = data
               return ("Success for making a session for the NFC certification request", 200)
          
     if request.method == 'GET' : 
          if 'nfc_tag_key' in session :
               session_data = session['nfc_tag_key']
               session.pop('nfc_tag_key', None)               
               return (session_data, 200)

          else : 
               return ("Wrong request", 400)         

@app.route("/qr_certification", methods=['GET', 'PUT']) ####
def qr_certification() : 
     data = request.get_json()
     user_id = data['user_id']
     center_equipment_id = data['center_equipment_id']

     user_centerequipment = get_qr_certification(user_id, center_equipment_id)
     if user_centerequipment is not None : 
          return (user_centerequipment, 200)
     else : 
          return ("Wrong request", 400)

@app.route("/users/<user_id>/workouts_report", methods=['GET']) ####
def get_workout_metrics_by_exercise_libs(user_id) : 
     pass 
