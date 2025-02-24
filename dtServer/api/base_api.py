from dtServer.app import *
from flask import request, abort
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.user_center_dao import userCenterDao
from dtServer.data.dao.user_account_dao import userAccountDao
from dtServer.data.dao.center_dao import centerDao
from dtServer.data.dao.center_member_dao import centerMemberDao
from dtServer.data.dao.exercise_library_dao import exerciseLibraryDao
from dtServer.data.dao.exerciselib_bodypart_dao import exerciseLibBodyPartDao
from dtServer.data.tranjection.signup_trans import signupTrans
from dtServer.data.dto.center_certification_dto import CenterCertificationDTO
from dtServer.data.dto.user_account_dto import UserAccountDTO
from dtServer.data.dto.user_auth_centers_dto import UserAuthCentersDTO
from dtServer.data.dto.app_lounge_dto import AppLoungeDTO
from dtServer.data.dao.user_centermember_dao import userCenterMemberDao

@app.route("/signup", methods = ['POST'])
def signup() : ###
    if request.method == 'POST' : 
          data = request.get_json()
          user_account = UserAccountDTO( data['user_account'] )
          user_info = data['user_info'] 

          valid_mes, r = user_account.valid_user_account()
          if not r : 
               return create_response(valid_mes, 400)

          login_id = user_account.get_login_id()

          if userAccountDao.is_user_account(login_id) : 
               return abort(400)
          
          user = signupTrans.insert_signup_data(user_info, user_account.get_user_account()) ####
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
          user_auth_centers = UserAuthCentersDTO( user_account['user']['id'] )
          return create_response(user_auth_centers.as_dict(), 200) 
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
          userCenterMemberDao.insert(user_id, center_id, center_member['id'])
          
          return create_response(user_center, 201)  
     
     if request.method == 'GET' : #
          data = request.get_json()
          user_id = data['user_id']
          center_id = data['center_id']

          user_center = userCenterDao.get_by_user_and_center(user_id, center_id)
          if user_center is None : 
               return "user's center authentication cannot found.", 404
          
          return create_response(user_center, 200)
     
@app.route("/lounge", methods=['GET'])
def get_lounge() : 
     data = request.get_json()
     user_id = data['user_id']
     center_id = data['center_id']

     from_date, to_date = get_recent_date_period()

     app_lounge = AppLoungeDTO(user_id, center_id, from_date, to_date)
     return create_response(app_lounge.as_dict(), 200)