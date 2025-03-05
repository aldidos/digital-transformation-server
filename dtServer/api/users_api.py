from dtServer.app import *
from flask import request, abort
from dtServer.data.dao.user.user_dao import userDao
from dtServer.data.dao.workout.workout_sessions_dao import workoutSessionDao
from dtServer.data.dao.workout.workouts_dao import workoutDao
from dtServer.data.tranjection.workout_data_trans import workoutDataTrans
from dtServer.data.dto.workout_data_dto import WorkoutSetMetricsDTO
from dtServer.data.report.builder.workout_report_builder import WorkoutReportBuilder
from dtServer.data.dao.workout.workout_metrics_dao import workoutMetricDao
from dtServer.data.dao.ormworkout.ormworkout_dao import ormWorkoutDao

@app.route("/users", methods=['POST'])
def post_users() : 
     data = request.get_json()
     user = userDao.save(data)
     if user is None : 
          return abort(400) 
     
     return create_response(user, 201)

@app.route("/users/<user_id>", methods=['GET'])
def get_req_users(user_id):          
     if request.method == 'GET' : 
          user = userDao.select_by_id(user_id)
          if user is None : 
               return abort(404)
          return create_response(user, 200)

@app.route("/users/<user_id>/workout_sessions/recent", methods=['GET']) 
def get_recent_user_workouts(user_id) : 
     from_date, to_date = get_recent_date_period()
     workout_sessions = workoutSessionDao.select_by_user_and_date_period(user_id, from_date, to_date)
     if not workout_sessions : 
          return abort(404)
     return create_response(workout_sessions, 200)

@app.route("/users/<user_id>/workout_sessions", methods=['POST', 'GET']) 
def get_post_user_workout_sessions(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()          
          workout_session = workoutSessionDao.save(data)
          return create_response(workout_session, 201)
     
     if request.method == 'GET' : 
          type = request.args.get('search_date')          
          if type == 'period' : 
               from_date, to_date = parse_request_args_from_to_dates(request)                     
               workout_sessions = workoutSessionDao.select_by_user_and_date_period(user_id, from_date, to_date)
               if not workout_sessions : 
                    return abort(404)
               return create_response(workout_sessions, 200)
          else : 
               date = request.args.get('date')
               workout_sessions = workoutSessionDao.select_by_user_and_date(user_id, date)
               if not workout_sessions : 
                    return abort(404)
               return create_response(workout_sessions, 200)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>", methods=['PATCH', 'GET']) 
def get_patch_user_workout_sessions(user_id, workout_session_id) : 
     if request.method == 'PATCH' : 
          data = request.get_json()
          workout_session = workoutSessionDao.save(data)
          return create_response(workout_session, 200)

     if request.method == 'GET' : 
          workout_session = workoutSessionDao.select_by_id(workout_session_id)
          if workout_session is None : 
               return abort(404)
          return create_response(workout_session, 200)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts", methods=['POST', 'GET']) 
def get_post_user_workouts(user_id, workout_session_id) : 
     if request.method == 'POST' : 
          data = request.get_json()         
          workout_id = workoutDao.insert(data)
          workout = workoutDao.select_by_id(workout_id)
          return create_response(workout, 201)

     if request.method == 'GET' : 
          workouts = workoutDao.select_by_workout_session(workout_session_id)
          if not workouts : 
               return abort(404)
          return create_response(workouts, 200)
     
@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>", methods=['PATCH', 'GET'])
def get_patch_user_workout(user_id, workout_session_id, workout_id) : 
     if request.method == 'PATCH' : 
          data = request.get_json()
          workout = workoutDao.save(data)
          return create_response(workout, 200)

     if request.method == 'GET' : 
          workout = workoutDao.select_by_id(workout_id)
          if workout is None : 
               return abort(404)
          return create_response(workout, 200)
     
@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets", methods = ['POST'])
def post_user_workoutsession_workout_set_metrics(user_id, workout_session_id, workout_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          workout_set_metrics_dto = WorkoutSetMetricsDTO(data)
          set_id = workoutDataTrans.insert_workout_set_metrics(workout_id, workout_set_metrics_dto)
          return create_response({ 'message' : 'Created workout set metrics', 'set_id' : set_id }, 201 )
     
@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/report", methods=['GET'])
def get_workout_session_report(user_id, workout_session_id) : 
     report = WorkoutReportBuilder.build_workout_session_report(workout_session_id)
     if not report : 
          return abort(404)
     return create_response(report.as_dict(), 200)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/report", methods=['GET'])
def get_user_workout_report(user_id, workout_session_id, workout_id) : 
     workout_report = WorkoutReportBuilder.build_workout_report(workout_id)
     if workout_report : 
          return create_response(workout_report.as_dict(), 200)
     return abort(404)
     
@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/<set_id>/report", methods = ['GET'])
def get_user_workout_set_report(user_id, workout_session_id, workout_id, set_id) :    
     report = WorkoutReportBuilder.build_workout_set_report(workout_id, set_id)
     if not report : 
          return abort(404)
     return create_response(report.as_dict(), 200)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/workout_metrics", methods = ['GET'])
def get_workout_sets_metrics(user_id, workout_session_id, workout_id) : 
     list_workout_metric_data = workoutMetricDao.select_workout_sets_data(workout_id)
     if not list_workout_metric_data : 
          return abort(404)
     return create_response(list_workout_metric_data, 200)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets/<set_id>/workout_metrics", methods = ['GET'])
def get_workout_set_metrics(user_id, workout_session_id, workout_id, set_id) : 
     list_workout_metrics = workoutMetricDao.select_workoutset_level_data(workout_id, set_id)
     if not list_workout_metrics : 
          return abort(404)
     return create_response(list_workout_metrics, 200)

@app.route("/users/<user_id>/workout_sessions/report", methods = ['GET'])
def get_user_workout_report_recent(user_id) : 
     from_date = request.args.get('from_date')
     to_date = request.args.get('to_date')

     if from_date > to_date : 
          return abort(400)
     
     report = WorkoutReportBuilder.build_date_period_workout_session_reports(user_id, from_date, to_date)
     if not report : 
          return abort(404)
          
     return create_response(report.as_dict(), 200)
     
@app.route("/users/<user_id>/workout_sessions/report/recent", methods = ['GET'])
def get_user_workoutreports_recent(user_id) : 
     from_date, to_date = get_recent_date_period()

     report = WorkoutReportBuilder.build_date_period_workout_session_reports(user_id, from_date, to_date)
     if not report : 
          return abort(404)
          
     return create_response(report.as_dict(), 200)

@app.route("/users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/report/recent", methods = ['GET'])
def get_recent_exercise_library_workout_report(user_id, exercise_library_id) : 
     report = WorkoutReportBuilder.build_recent_workout_reports_by_exercise_library(user_id, exercise_library_id)
     if not report : 
          return abort(404)
     return create_response(report.as_dict(), 200)

@app.route("/users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/<set_number>/report/recent", methods=['GET'])
def get_user_recent_exercise_lib_set_report(user_id, exercise_library_id, set_number) :      
     report = WorkoutReportBuilder.build_recent_workout_set_report_by_exercise_library(user_id, exercise_library_id, set_number)
     if not report : 
          return abort(404)
     return create_response(report.as_dict(), 200)

@app.route("/users/<user_id>/workouts/equipments/<equipment_id>/recent", methods=['GET'])
def get_user_workouts_recent_by_equipment(user_id, equipment_id) : 
     workouts = workoutDao.get_recent_by_equipment(user_id, equipment_id)
     if not workouts : 
          return abort(404)
     return create_response( workouts, 200)

@app.route("/users/<user_id>/workouts/equipments/<equipment_id>/most_recent", methods=['GET'])
def get_user_workouts_most_recent_by_equipment(user_id, equipment_id) : 
     workout = workoutDao.get_most_recent_by_equipment(user_id, equipment_id)
     if not workout : 
          return abort(404)
     return create_response( workout, 200)
     
@app.route("/users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/recent", methods=['GET'])
def get_user_workouts_recent_by_exercise_library(user_id, exercise_library_id) : 
     workouts = workoutDao.get_recent_by_exercise_library(user_id, exercise_library_id)
     if not workouts : 
          return abort(404)
     return create_response( workouts, 200)

@app.route("/users/<user_id>/workouts/exercise_libraries/<exercise_library_id>/most_recent", methods=['GET'])
def get_user_workouts_most_recent_by_exercise_library(user_id, exercise_library_id) :
     workout = workoutDao.get_most_recent_by_exercise_library(user_id, exercise_library_id)
     if not workout : 
          return abort(404)
     return create_response( workout, 200)

@app.route("/users/<user_id>/workouts/body_parts/<body_part_id>/recent", methods=['GET'])
def get_user_workouts_recent_by_body_part(user_id, body_part_id) : 
     workouts = workoutDao.get_recent_by_body_part(user_id, body_part_id)
     if not workouts : 
          return abort(404)
     return create_response( workouts, 200)

@app.route("/users/<user_id>/workouts/body_parts/<body_part_id>/most_recent", methods=['GET'])
def get_user_workouts_most_recent_by_body_part(user_id, body_part_id) : 
     workout = workoutDao.get_most_recent_by_body_part(user_id, body_part_id)
     if not workout : 
          return abort(404)
     return create_response(workout, 200)

@app.route("/users/<user_id>/1RMS/equipments/<equipment_id>/recent", methods=['GET'])
def get_users_recent_1RMs_by_equipment(user_id, equipment_id) : 
     ormworkouts = ormWorkoutDao.get_recent_by_equipment(user_id, equipment_id)
     if not ormworkouts : 
          return abort(404)
     return create_response(ormworkouts, 200)

@app.route("/users/<user_id>/1RMS/equipments/<equipment_id>/most_recent", methods=['GET'])
def get_users_most_recent_1RM_by_equipment(user_id, equipment_id) : 
     ormworkout = ormWorkoutDao.get_most_recent_by_equipment(user_id, equipment_id)
     if not ormworkout : 
          return abort(404)
     return create_response(ormworkout, 200)