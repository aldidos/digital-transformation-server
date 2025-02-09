from flask import request, abort
from dtServer.app import *
from dtServer.data.dao.center_dao import centerDao
from dtServer.data.dao.center_member_dao import centerMemberDao
from dtServer.data.dao.center_staff_dao import centerStaffDao
from dtServer.data.dao.center_equipment_dao import centerEquipmentDao

@app.route("/centers", methods=['POST'])
def centers() : 
     data = request.get_json()
     center = centerDao.save(data)
     if center is None :
          return abort(400)
     return (center, 201)

@app.route("/centers/<center_id>", methods=['GET'])
def center(center_id : int) : 
     center = centerDao.get_by_id(center_id) 
     if center is None : 
          return abort(400)
     return (center, 200)

@app.route("/centers/<center_id>/members", methods=['GET', 'POST']) ####
def get_post_center_members(center_id : int) :
     if request.method == 'POST' : 
          data = request.get_json()
          center_member = centerMemberDao.get(center_id, data['name'], data['birth_day'], data['contact'])
          if center_member is None : 
               center_member = centerMemberDao.save(data) 
               return (center_member, 201)
          return "The center member is already in the center.", 400
               
     if request.method == 'GET' : 
          data = request.get_json()
          name = data['name']
          birthday = data['birth_day']
          contact = data['contact']
          center_member = centerMemberDao.get(center_id, name, birthday, contact)
          if center_member is None : 
               return abort(404)
          return (center_member, 200)
     
@app.route("/centers/<center_id>/members/<member_id>", methods=['PATCH']) ####
def patch_center_members(center_id : int, member_id : int) :
     if request.method == 'PATCH' : 
          data = request.get_json()
          center_member = centerMemberDao.save( data )
          return center_member, 200 
   
@app.route("/centers/<center_id>/staffs", methods=['GET', 'POST'])
def center_staffs(center_id : int) : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_staff = centerStaffDao.save(data)
          if center_staff is None :
               return abort(400) 
          return (center_staff, 201)
     
     if request.method == 'GET' : 
          center_staffs = centerStaffDao.select_by_center_id(center_id) 
          if not center_staffs : 
               return abort(404)
          return (center_staffs, 200)

@app.route("/centers/<center_id>/equipments", methods=['POST', 'GET'])
def center_equipments(center_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          center_equipment = centerEquipmentDao.save(data)
          if center_equipment is None : 
               return abort(400)
          return center_equipment, 201

     if request.method == 'GET' : 
          center_equipments = centerEquipmentDao.select_by_center_id(center_id)
          if not center_equipments : 
               return abort(404)
          return (center_equipments, 200) 
