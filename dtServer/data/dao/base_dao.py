from playhouse.shortcuts import model_to_dict, dict_to_model

class BaseDAO : 

    def save_model(self, model) : 
        model.save()
        return model_to_dict(model)
