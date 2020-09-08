import json

class GameMap:
    local_path=""
    grid=[]

    def __init__(self,key,size,context):
        self.key=key
        self.size=size
        self.context=context
        # create local path if it doesn't exist

    def make_new_map(self):
        pass

    def save_map(self,key,map_dict):
        with open(local_path+key,'w') as json_file:
            json.dump(map_dict,json_file)

    def load_map(self,key):
        data={}
        with open(local_path+key) as f:
            data= json.load(f)
        return data

