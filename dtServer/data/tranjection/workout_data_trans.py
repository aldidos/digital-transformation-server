from dtServer.data.model.base_model import db_proxy
from dtServer.data.dao.workout_sessions_dao import workoutSessionDao
from dtServer.data.dao.workouts_dao import workoutDao
from dtServer.data.dao.workout_set_dao import workoutSetDao
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao
from dtServer.data.form.workout_data_form import WorkoutDataForm

class WorkoutDataTrans : 

    def insert_workout(self, workout_session_id,  data : WorkoutDataForm ) :
        workout = data.get_workout()
        workout['workout_session_id'] = workout_session_id
        return workoutDao.insert(workout)
    
    def insert_workout_set_dataset(self, workout_id, dataset : dict) : 
        workout_set = dataset['workout_set']
        workout_set['workout_id'] = workout_id
        workout_set_id = workoutSetDao.insert(workout_set)

        workout_metrics = dataset['workout_metrics']
        for workout_metric in workout_metrics : 
            workout_metric['workout_set_id'] = workout_set_id

        workoutMetricDao.insert_many(workout_metrics) 
    
    def insert_workout_sets(self, workout_id : int, data : WorkoutDataForm) :         
        for workout_set_dataset in data.get_workout_sets() : 
            self.insert_workout_set_dataset(workout_id, workout_set_dataset)

    def insert(self, workout_session_id, data : WorkoutDataForm) : 
        with db_proxy.atomic() :             
            workout_id = self.insert_workout(workout_session_id, data)
            self.insert_workout_sets(workout_id, data)

workoutDataTrans = WorkoutDataTrans()