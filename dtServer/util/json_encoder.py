from datetime import datetime, date
import json

class DateFormatEncoder(json.JSONEncoder) : 

    def default(self, o):
        if isinstance(o, date) : 
            return o.isoformat() 
        elif isinstance(o, datetime) : 
            return o.isoformat()
        
        return super().default(o)
    
def encode(o : dict) : 
    encoder = DateFormatEncoder()
    return encoder.encode(o)