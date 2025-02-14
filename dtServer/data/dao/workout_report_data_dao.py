from dtServer.data.dao.workout_set_dao import workoutSetDao
from dtServer.data.model.workout_set import WorkoutSet
from dtServer.data.model.workout_metrics import WorkoutMetrics
from dtServer.data.dao.workout_metrics_dao import workoutMetricDao

class WorkoutReportDataDao : 

    def get_recent_set_data(self, user_id, exercise_library_id, set) : 
        recent_workoutset = workoutSetDao.get_recent_by_exerciselibrary(user_id, exercise_library_id, set)

        if not recent_workoutset : 
            return None

        workout_set_id = recent_workoutset['id']
        workout_id = recent_workoutset['workout']['id']

        return self.get_set_data(workout_id, workout_set_id)
    
    def get_set_data(self, workout_id, workout_set_id) : 
        return workoutMetricDao.select_workoutset_level_data(workout_id, workout_set_id)
    
    def get_workout_data(self, workout_id) : 
        return workoutMetricDao.select_woekout_level_data(workout_id)

    def get_workoutsession_data(self, workout_session_id) : 
        return workoutMetricDao.select_by_user_and_dateperiod(workout_session_id)
    
workoutReportDataDao = WorkoutReportDataDao()