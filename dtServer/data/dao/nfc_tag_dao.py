from dtServer.data.dao.base_dao import BaseDAO
from dtServer.data.model.nfc_tag import NFCTag, db_proxy, model_to_dict_or_none
from playhouse.shortcuts import model_to_dict, dict_to_model

class NFCTagDao(BaseDAO) : 

    def save(self, data : dict) :         
        return self.save_model( dict_to_model(NFCTag, data) )
    
    def create_nfc_access(self, nfc_tag_id, center_equipment_id) : 
        data = {
            'nfc_tag_id' : nfc_tag_id, 
            'center_equipment' : center_equipment_id
        }
        return self.save(data)

    def select_by_nfc_tag_id(self, nfc_tag_id) : 
        nfc_tag = NFCTag.get_or_none( NFCTag.nfc_tag_id == nfc_tag_id )
        return model_to_dict_or_none(nfc_tag)

    def insert_many(self, list_data) : 
        with db_proxy.atomic() :
            NFCTag.insert_many(list_data).execute()

nfcTagDao = NFCTagDao()