from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao
from dtServer.data.dao.workouts_dao import workoutDao
from dtServer.data.dao.workout_set_dao import workoutSetDao
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.form.workout_data_form import WorkoutSetMetricsDTO

class WorkoutDataTrans : 

    def insert_workout(self, workout_session_id,  data : WorkoutSetMetricsDTO ) :
        workout = data.get_workout()
        workout['workout_session_id'] = workout_session_id
        return workoutDao.insert(workout)
    
    def insert_workout_set_metrics(self, workout_id, dataset : WorkoutSetMetricsDTO) :
        with db_proxy.atomic() :  
            workout_set = dataset.get_workout_set()
            workout_set['workout_id'] = workout_id
            workout_set_id = workoutSetDao.insert(workout_set)

            workout_metrics = dataset.get_workout_metrics()
            for workout_metric in workout_metrics : 
                workout_metric['workout_set'] = workout_set_id

            workoutMetricDao.insert_many(workout_metrics) 

workoutDataTrans = WorkoutDataTrans()