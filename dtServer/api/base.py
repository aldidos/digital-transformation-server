from dtServer.app import *
from flask import request, abort, session
from dtServer.data.dao.user_center_dao import userCenterDao
from dtServer.data.dao.user_account_dao import userAccountDao
from dtServer.data.dao.center_dao import centerDao
from dtServer.data.dao.center_member_dao import centerMemberDao
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao
from dtServer.data.dao.nfc_tag_dao import nfcTagDao
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.dao.signup_dao import signupDao
from dtServer.data.dao.app_base_data_dao import appBaseDataDao

@app.route("/nfc_certification", methods=['POST', "GET"])
def nfc_certification() : 
     if request.method == 'POST' :
          data = request.get_json()
          nfc_tag_id = data['nfc_tag_id']
          user_id = data['user_id']
          center_equipment_id = data['center_equipment_id']

          nfc_tag = nfcTagDao.select_by_nfc_tag_id(nfc_tag_id)
          if nfc_tag is None : 
               return abort(400)
          else :                
               session['nfc_tag_certification'] = {
                    'nfc_tag_id' : nfc_tag_id, 
                    'user' : user_id, 
                    'center_equipment' : center_equipment_id
               }
               return (RES_MES_200, 200) 
          
     if request.method == 'GET' : 
          if 'nfc_tag_certification' in session : 
               session_data = session['nfc_tag_certification']
               machine_init_data = appBaseDataDao.get_machine_init_data(session_data['user'], session_data['center_equipment'])

               return create_response( machine_init_data, 200)
          
          return abort(400)

@app.route("/qr_certification", methods=['PUT', 'GET']) ####
def qr_certification() : 
     data = request.get_json()
     if request.method == 'PUT' :  
          user = data['user_id']
          center_equipment = data['center_equipment_id']
          session['qr_certification'] = {
               'user' : user, 
               'center_equipment' : center_equipment
          }

          return (RES_MES_200, 200)
     if request.method == 'GET' :           
          if 'qr_certification' in session : 
               session_data = session['qr_certification']
               machine_init_data = appBaseDataDao.get_machine_init_data(session_data['user'], session_data['center_equipment'])
               return create_response(machine_init_data, 200)          
          return abort(400)

@app.route("/signup", methods = ['POST'])
def signup() : ###
    if request.method == 'POST' : 
          data = request.get_json()
          user_account = data['user_account']
          user_info = data['user_info'] 

          login_id = user_account['login_id']
          
          prev_user_account = userAccountDao.get_by_loginid(login_id)

          if prev_user_account == None : 
               user = signupDao.insert_signup_data(user_info, user_account) 
               return create_response(user, 201)
          else : 
               return abort(400)

@app.route("/signin", methods=['GET']) 
def signin() : 
     data = request.get_json()
     login_id = data['login_id'] 
     login_pw = data['login_pw']
     
     user_account = userAccountDao.get_by_loginid(login_id)

     if user_account is None : 
        return abort(400)
     
     if login_pw == user_account['login_pw'] : 
          app_init_data = appBaseDataDao.get_user_app_init_data(user_account['user']['id'])
          return create_response(app_init_data, 200) 
     return abort(400)

@app.route("/exercise_libraries", methods=['GET'])
def get_req_exercise_libraries() : 
     if request.method == 'GET' : 
          exercise_libs = exerciseLibraryDao.select_all() 
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
          return create_response(data, 200)
     
@app.route("/center_authentication", methods=['PUT', 'GET'])
def center_authentication() : ###
     if request.method == 'PUT' : 
          data = request.get_json()
          center_name = data['center_name']
          center_address = data['center_address']
          user_id = data['user_id']
          user_name = data['user_name']
          birthday = data['birthday']
          contact = data['contact'] 

          center = centerDao.get_by_name_and_address(center_name, center_address)
          if center is None : ## 센터가 플랫폼에 등록되지 않은 경우
               return ("The center is not involved in out service", 400) 
          
          center_id = center['id']
          user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
          if user_center is not None : ## 사용자 센터 인증이 이미 되어 있는 경우
               # user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
               return ("The user and center has been authenticated already", 200)
          
          center_member = centerMemberDao.get(center_id, user_name, birthday, contact)
          if center_member is None : ## 사용자가 센터 회원이 아닌 경우
               return ('The user is not a member of the center', 400)
          
          user_center = userCenterDao.create_user_center(user_id, center_id)
          return create_response(user_center, 201)  #### 
     
     if request.method == 'GET' : #
          data = request.get_json()
          user_id = data['user_id']
          center_id = data['center_id']

          user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
          if user_center is None : 
               return abort(404) ## user's center authentication cannot found.
          
          name = user_center['user']['name']
          birthday = user_center['user']['birthday']
          contact = user_center['user']['contact']

          center_member = centerMemberDao.get(center_id, name, birthday, contact)

          return create_response(center_member, 200)