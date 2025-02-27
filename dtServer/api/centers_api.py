from flask import request, abort
from dtServer.app import *
from dtServer.data.dao.center.center_dao import centerDao
from dtServer.data.dao.center.center_member_dao import centerMemberDao
from dtServer.data.dao.center.center_staff_dao import centerStaffDao
from dtServer.data.dao.center.center_equipment_dao import centerEquipmentDao
from dtServer.api.exercise_machine_auth import add_machine_key_value, get_key_data, pop_key_data
from dtServer.data.dto.center_equipment_auth_dto import CenterEquipmentAuthDTO

@app.route("/centers", methods=['POST'])
def centers() : 
     data = request.get_json()
     center = centerDao.save(data)
     if center is None :
          return abort(400)
     return create_response(center, 201)

@app.route("/centers/<center_id>", methods=['GET'])
def center(center_id : int) : 
     center = centerDao.get_by_id(center_id) 
     if center is None : 
          return abort(400)
     return create_response(center, 200)

@app.route("/centers/<center_id>/members", methods=['GET', 'POST']) ####
def get_post_center_members(center_id : int) :
     if request.method == 'POST' : 
          data = request.get_json()
          center_member = centerMemberDao.get(center_id, data['name'], data['birth_day'], data['contact'])
          if center_member is None : 
               center_member = centerMemberDao.save(data) 
               return create_response(center_member, 201)
          return "The center member is already in the center.", 400
               
     if request.method == 'GET' : 
          center_members = centerMemberDao.select_by_center_id(center_id)
          if not center_members : 
               return abort(404)
          return create_response(center_members, 200)          
     
@app.route("/centers/<center_id>/members/<member_id>", methods=['PATCH', 'GET']) 
def patch_center_members(center_id : int, member_id : int) :
     if request.method == 'PATCH' : 
          data = request.get_json()
          center_member = centerMemberDao.save( data )
          return create_response(center_member, 200)
     
     if request.method == 'GET' : 
          center_member = centerMemberDao.get_by_id(member_id)
          if center_member == None : 
               abort(404)
          return center_member, 200          
   
@app.route("/centers/<center_id>/staffs", methods=['GET', 'POST'])
def center_staffs(center_id : int) : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_staff = centerStaffDao.save(data)
          if center_staff is None :
               return abort(400) 
          return create_response(center_staff, 201)
     
     if request.method == 'GET' : 
          center_staffs = centerStaffDao.select_by_center_id(center_id) 
          if not center_staffs : 
               return abort(404)
          return create_response(center_staffs, 200)

@app.route("/centers/<center_id>/equipments", methods=['POST', 'GET'])
def center_equipments(center_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_equipment = centerEquipmentDao.save(data)
          if center_equipment is None : 
               return abort(400)
          return create_response(center_equipment, 201)

     if request.method == 'GET' : 
          center_equipments = centerEquipmentDao.select_by_center_id(center_id)
          if not center_equipments : 
               return abort(404)
          return create_response(center_equipments, 200)
     
@app.route("/centers/<center_id>/equipments/<center_equipment_id>", methods=['PATCH', 'GET'])
def patch_center_equipments(center_id, center_equipment_id) : 
     if request.method == 'PATCH' : 
          data = request.get_json()
          centerEquipmentDao.save(data)
          return create_response("OK", 200)

     if request.method == 'GET' : 
          center_equipments = centerEquipmentDao.get_by_id(center_equipment_id)
          if not center_equipments : 
               return abort(404)
          return create_response(center_equipments, 200)
     
@app.route("/centers/<center_id>/equipments/<center_equipment_id>/auth", methods=['GET', 'PUT'])
def get_put_center_equipemnt_auth(center_id, center_equipment_id) :
     if request.method == 'PUT' : 
          data = request.get_json()
          machine_key = data['machine_key']
          user_id = data['user_id']
          workout_session_id = data['workout_session_id']
          machine_auth_data = {
               'user_id' : user_id, 
               'workout_session_id' : workout_session_id,
               'center_equipment_id' : center_equipment_id
          }

          if get_key_data(machine_key) : 
               return create_response('Authentication request for the center equipment has already been maed', 400)

          add_machine_key_value(machine_key, machine_auth_data)

          return create_response('OK', 200)
     
     if request.method == 'GET' : 
          data = request.get_json()
          machine_key = data['machine_key']

          machine_auth_data = get_key_data(machine_key)

          if not machine_auth_data : 
               return create_response('The requested machine key cannot found', 404)
          
          pop_key_data(machine_key) ####

          center_equipment_auth_dto = CenterEquipmentAuthDTO(machine_auth_data['user_id'], machine_auth_data['workout_session_id'], machine_auth_data['center_equipment_id'])

          return create_response(center_equipment_auth_dto.as_dict(), 200)
     
@app.route("/centers/<center_id>/equipments/<center_equipment_id>/leave", methods=['PUT'])
def put_center_equipemnt_leave(center_id, center_equipment_id) :
     data = request.get_json()
     user_id = data['user_id']

     center_equipment = centerEquipmentDao.get_by_id(center_equipment_id)
     center_equipment['usage'] = False
     centerEquipmentDao.save(center_equipment)

     return create_response('OK', 200)