from dtServer.app import *
from flask import request, abort
from dtServer.data.dao.user_dao import userDao
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao
from dtServer.data.dao.workouts_dao import workoutDao
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.dao.user_survey_dao import userSurveyDao
from dtServer.data.dao.weight_metric_session_dao import weightMetricSession
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.form.workout_data_form import WorkoutDataForm 
from dtServer.data.tranjection.workout_data_trans import workoutDataTrans

@app.route("/users/<user_id>/weight_metric_sessions", methods=['GET', 'POST']) ####
def get_post_req_user_exercise_metric(user_id) :
     if request.method == 'POST' or request.method == 'PATCH' : 
          data = request.get_json()
          user_exercise_weight = weightMetricSession.save(data)
          return create_response(user_exercise_weight, 201)
     
     if request.method == 'GET' : 
          from_date, to_date = parse_request_args_from_to_dates(request)
          user_weight_metric = weightMetricSession.select_by_date_period(from_date, to_date)
          if user_weight_metric is None : 
               return abort(404) 
          return create_response(user_weight_metric, 200)
     
@app.route("/users/<user_id>/weight_metric_sessions/<weight_metric_session_id>", methods=['GET', 'PATCH']) ####
def get_patch_req_user_exercise_metric(user_id, weight_metric_session_id) :
     if request.method == 'PATCH' or request.method == 'PATCH' : 
          data = request.get_json()
          user_exercise_weight = weightMetricSession.save(data)
          return create_response(user_exercise_weight, 200)
     
     if request.method == 'GET' : 
          user_weight_metric = weightMetricSession.select_by_id(weight_metric_session_id)
          if user_weight_metric is None : 
               return abort(404)               
          return create_response(user_weight_metric, 200)
     
@app.route("/users/<user_id>/survey", methods=['GET', 'POST', 'PATCH']) ####
def users_survey(user_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          user_survey = userSurveyDao.save(data) 
          if user_survey is None : 
               return abort(400)               
          return create_response(user_survey, 201) 

     if request.method == 'GET' : 
          user_survey = userSurveyDao.select_by_user(user_id)
          if user_survey is None : 
               return abort(404)  
          return create_response(user_survey, 200)
     
     if request.method == 'PATCH' : 
          data = request.get_json()
          user_survey = userSurveyDao.save(data) 
          return create_response(user_survey, 200)

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
          workout_data_form = WorkoutDataForm(data)
          workoutDataTrans.insert(workout_session_id, workout_data_form)
          
          return create_response('Created user''s workout data', 201)

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

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/workout_metrics", methods=['POST']) 
def get_post_user_workout_metrics(user_id, workout_session_id, workout_id) : 
     if request.method == 'POST' : 
          data = request.get_json()
          workout_metric_ids = workoutMetricDao.insert_many(data)
          workoutDataDao.insert_many(user_id, workout_session_id, workout_id, workout_metric_ids)          
          return RES_MES_201, 201

@app.route("/users/<user_id>/workout_sessions/reports/recent", methods=['GET']) 
def get_user_workoutsessions_reports_recent(user_id) :      
     from_date, to_date = get_recent_date_period() 
     list_data = workoutDataDao.select_by_date_period(user_id, from_date, to_date) 
     res = get_workout_metric_stat(list_data) 
     if not res :
          return abort(404)
     return create_response(res, 200)

@app.route("/users/<user_id>/workout_sessions/reports", methods=['GET']) 
def get_user_workoutsessions_reports(user_id) : 
     search_date = request.args.get('search_date')
     if search_date == 'period' :           
          from_date, to_date = parse_request_args_from_to_dates(request)
          list_data = workoutDataDao.select_by_date_period(user_id, from_date, to_date) 
          res = get_workout_metric_stat(list_data) 
          if not res :
               return abort(404)
          return res, 200 
     elif search_date == 'date' : 
          date = request.args.get('date')
          list_data = workoutDataDao.select_by_date(user_id, date) 
          res = get_workout_metric_stat(list_data)
          if not res :
               return abort(404)
          return create_response(res, 200)
     
     return abort(400)

@app.route("/users/<user_id>/workout_sessions/<workout_session_id>/report", methods=['GET']) 
def get_user_workoutsession_report(user_id, workout_session_id) : 
     list_data = workoutDataDao.select(user_id, workout_session_id)
     res = get_workout_metric_stat(list_data) 
     if not res :
               return abort(404)
     return create_response(res, 200)