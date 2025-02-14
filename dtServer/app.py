from flask import Flask, request, make_response
from dtServer.data.conn import make_database_connection, db_proxy
from datetime import datetime, timedelta
from dtServer.data.statistics.stat_workout import statWorkout
import json

def parse_date_str(datestr) : 
     return datetime.strptime(datestr, '%Y-%m-%d')

def parse_request_args_from_to_dates(request) : 
     arg_from_date = request.args.get('from_date')
     arg_to_date = request.args.get('to_date')

     from_date = parse_date_str( arg_from_date )
     to_date = parse_date_str(arg_to_date)

     return from_date, to_date

def get_recent_date_period() : 
     to_date = datetime.now()
     from_date = to_date - timedelta(days = 7)   

     return from_date, to_date

def get_workout_metric_stat(list_data) :           
     if list_data : 
          return statWorkout.stat(list_data)
     return []

def json_to_dict(data) : 
     return json.loads(data)

app = Flask(__name__)
app.secret_key = b'_@sD2&f^L(i8p]2#mHzVs1@^&gj]'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['JSON_AS_ASCII'] = False

RES_MES_200 = 'Request OK'
RES_MES_201 = 'Resource created'
RES_MES_400 = 'Bad request'
RES_MES_404 = 'Not Found'

db_conn = make_database_connection()
db_proxy.initialize(db_conn)

## For utf-8 encoding of text.
def create_response(data, status) : 
     return make_response( json.dumps(data, ensure_ascii=False, default = str, indent=4), status)

def check_header_app_token() :      
    APP_TOKEN_VALUE = 'aDiQ2X@&a$!2hcoIJdtyaYwBcghP2)kc'
    token = request.headers.get('app-token')
    if token == APP_TOKEN_VALUE : 
        return True
    return False

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
     return RES_MES_400, 400

@app.errorhandler(404)
def request_error_not_found(e) : 
     return RES_MES_404, 404