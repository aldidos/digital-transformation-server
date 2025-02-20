from dtServer.app import *
from flask import request, abort, session
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.user_center_dao import userCenterDao
from dtServer.data.dao.user_account_dao import userAccountDao
from dtServer.data.dao.center_dao import centerDao
from dtServer.data.dao.center_member_dao import centerMemberDao
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao
from dtServer.data.dao.nfc_tag_dao import nfcTagDao
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.tranjection.app_base_data_trans import appBaseDataTrans
from dtServer.data.tranjection.machin_app_base_data_trans import machinAppBaseDataTrans
from dtServer.data.tranjection.signup_trans import signupTrans
from dtServer.data.dto.machine_certification_dto import MachineCertificationDTO
from dtServer.data.dto.center_certification_dto import CenterCertificationDTO

SESSION_MACHINE_CERTIFICATION = 'machine_certification'

def make_session(key : str, data : dict) : 
     if key in session : 
          return False     
     session[key] = data
     return True

def destroy_session(key) : 
     if key in session :
           session.pop(key, None)
           return "Destroyed workout session", 200
     return abort(400)

@app.route("/nfc_certification", methods=['PUT', "GET"])
def nfc_certification() : 
     if request.method == 'PUT' :
          data = request.get_json()
          form = MachineCertificationDTO(data)

          nfc_tag = nfcTagDao.select_by_nfc_tag_id( form.get_nfc_tag_id() )
          if nfc_tag is None : 
               return abort(400)
          else : 
               if make_session(SESSION_MACHINE_CERTIFICATION, form.get_data() ) : 
                    return (RES_MES_200, 200) 
               return "The user has unfinished machine certification", 400               
          
     if request.method == 'GET' : 
          if SESSION_MACHINE_CERTIFICATION in session : 
               session_data = session[SESSION_MACHINE_CERTIFICATION]
               base_data = machinAppBaseDataTrans.get_data( session_data['user_id'], session_data['center_equipment_id'], session_data['workout_session_id'] ) 

               return create_response( base_data, 200)
          
          return abort(404)

@app.route("/qr_certification", methods=['PUT', 'GET']) ####
def qr_certification() :      
     if request.method == 'PUT' :  
          data = request.get_json()
          form = MachineCertificationDTO(data)          

          if make_session(SESSION_MACHINE_CERTIFICATION, form.get_data() ) : 
               return (RES_MES_200, 200)          
          return "The user has unfinished machine certification", 400     
     
     if request.method == 'GET' : 
          if SESSION_MACHINE_CERTIFICATION in session : 
               session_data = session[SESSION_MACHINE_CERTIFICATION]
               base_data = machinAppBaseDataTrans.get_data( session_data['user_id'], session_data['center_equipment_id'], session_data['workout_session_id'] ) 
               return create_response(base_data, 200) 
          return abort(404)
     
@app.route("/end_wokrout_session", methods=['PUT'])
def end_workout() : 
      return destroy_session( SESSION_MACHINE_CERTIFICATION )

def valid_user_account(user_account) : 
     login_id = user_account['login_id']
     login_pw = user_account['login_pw']
     if len(login_id) < 4 : 
          return 'THIS MESSGAE IS SENT DURING DEVELOPING : the length of login_id must be over 4', False

     if len(login_pw) < 4 : 
          return 'THIS MESSGAE IS SENT DURING DEVELOPING : the length of login_pw must be over 4', False

     return 'THIS MESSGAE IS SENT DURING DEVELOPING : the login id and pw can be used', True
      
@app.route("/signup", methods = ['POST'])
def signup() : ###
    if request.method == 'POST' : 
          data = request.get_json()
          user_account = data['user_account']
          user_info = data['user_info']           

          valid_mes, r = valid_user_account(user_account)
          if not r : 
               return create_response(valid_mes, 400)

          login_id = user_account['login_id']
          login_pw = user_account['login_pw']          

          if userAccountDao.is_user_account(login_id) : 
               return abort(400)
          
          user = signupTrans.insert_signup_data(user_info, user_account) ####
          return create_response(user, 201) 

@app.route("/signin", methods=['PUT']) 
def signin() : 
     data = request.get_json()
     login_id = data['login_id'] 
     login_pw = data['login_pw']
     
     user_account = userAccountDao.get_by_loginid(login_id)

     if user_account is None : 
        return abort(400)
     
     if login_pw == user_account['login_pw'] : 
          app_base_data = appBaseDataTrans.get_data(user_account['user']['id'])
          return create_response(app_base_data, 200) 
     return abort(400)

@app.route("/exercise_libraries", methods=['GET'])
def get_req_exercise_libraries() : 
     if request.method == 'GET' : 
          exercise_libs = exerciseLibraryDao.select_all() 
          return create_response(exercise_libs, 200)
     
@app.route("/exercise_libraries/<equipment_id>", methods=['GET'])
def get_exercise_libraries_by_equipment(equipment_id) : 
     if request.method == 'GET' : 
          exercise_libs = exerciseLibraryDao.select_by_equipment(equipment_id)
          if not exercise_libs : 
               return abort(404)
          
          return create_response(exercise_libs, 200)
     
@app.route("/exerciselib_bodyparts", methods=['GET'])
def get_req_exerciselib_bodyparts() : 
     if request.method == 'GET' : 
          exericselib_bodyparts = exerciseLibBodyPartDao.select_all()
          return create_response(exericselib_bodyparts, 200)
     
@app.route("/exerciselib_bodyparts/<exerciselib_id>/<body_part_id>", methods=['GET'])
def get_req_exerciselib_bodypart(exerciselib_id, body_part_id) : 
     if request.method == 'GET' : 
          data = exerciseLibBodyPartDao.get_by_exercise_library_id_and_body_part_id(exerciselib_id, body_part_id)
          if data : 
               return create_response(data, 200)
          return abort(404)
     
@app.route("/center_authentication", methods=['PUT', 'GET'])
def center_authentication() : ###
     if request.method == 'PUT' : 
          data = request.get_json()
          form = CenterCertificationDTO(data)

          user_id = form.get_user_id()

          center = centerDao.get_by_name_and_address(form.get_center_name(), form.get_center_address())
          if center is None : ## 센터가 플랫폼에 등록되지 않은 경우
               return ("The center is not involved in out service", 400) 
          
          center_id = center['id']
          user_center = userCenterDao.get_by_user_and_center( user_id, center_id)
          if user_center is not None : ## 사용자 센터 인증이 이미 되어 있는 경우
               # user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
               return ("The user and center has been authenticated already", 400)
          
          user = userDao.select_by_id( user_id )
          center_member = centerMemberDao.get(center_id, user['name'], user['birthday'], user['contact'])
          if center_member is None : ## 사용자가 센터 회원이 아닌 경우
               return ('The user is not a member of the center', 400)
          
          user_center = userCenterDao.create_user_center(user_id, center_id)
          return create_response(user_center, 201)  
     
     if request.method == 'GET' : #
          data = request.get_json()
          user_id = data['user_id']
          center_id = data['center_id']

          user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
          if user_center is None : 
               return "user's center authentication cannot found.", 404
          
          return create_response(user_center, 200)