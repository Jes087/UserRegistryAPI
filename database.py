import os
import json
from typing import Dict

class Database:

    @classmethod
    def select_all(cls):
        if not os.path.isfile('user_table.json'):
            with open('user_table.json','w') as f:
                json.dump([],f)
        
        with open('user_table.json','r') as f:
            data=json.load(f)
        return data

    @classmethod
    def insert(cls,data:Dict):
        with open('user_table.json','w') as f:
            json.dump(data,f)
        
    @classmethod
    def confirm_last_save(cls):
        with open('user_table.json','r') as f:
            data=json.load(f)
        return data[-1]
    
    @classmethod
    def select(cls,user_id:str):
        with open('user_table.json','r') as f:
            data=json.load(f)

        for d in data:
            if d["id"]==user_id:
                return d
        
        return []




    