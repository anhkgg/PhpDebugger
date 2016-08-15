# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import ConfigParser
import base64
import json

class ide_config:
    def __init__(self):
        pass
    
    def add_watch_variable(self,name):
        return self._add_data("watch_variables",name)
    
    def remove_watch_variable(self,name):
        print name
        return self._remove_data("watch_variables",name)
        
    def get_watch_variable(self):
        return self._get_data("watch_variables")
    
    def add_watch_file(self,path):
        return self._add_data("watch_files",path)
    
    def remove_watch_file(self,path):
        return self._remove_data("watch_files",path)
        
    def get_watch_file(self):
        return self._get_data("watch_files")
    
    def add_folder(self,path):
        return self._add_data("folders",path)
        
    def remove_folder(self,path):
        return self._remove_data("folders",path)

    def get_folders(self):
        return self._get_data("folders")
    
    def _add_data(self,type,data):
        datas = self._get_data(type)
        if data in datas:
            return datas
        datas.append(data)
        self._save_data(type, datas)
        return datas
        
    def _remove_data(self,type,data):
        datas = self._get_data(type)
        if data not in datas:
            return datas
        datas.remove(data)
        self._save_data(type, datas)
        return datas
    
    def _get_data(self,type):
        config = ConfigParser.ConfigParser()
        with open('ide.cfg','r') as cfgfile: 
            config.readfp(cfgfile) 
        
        if False == config.has_section(type):
            return []

        if "data" not in config.options(type):
            return []
            
        output_data = config.get(type, "data")
        temp = base64.b64decode(output_data)
        data = json.loads(temp)
        if isinstance(data,list):
            return data
        else:
            return []
        
    def _save_data(self, type, data):
        config_r = ConfigParser.ConfigParser()
        config_r.read('ide.cfg')
        if False == config_r.has_section(type):
            config_r.add_section(type)
        
        input_data = base64.b64encode(json.dumps(data))
        config_r.set(type, "data", input_data)
        with open('ide.cfg', 'wb') as configfile:
            config_r.write(configfile)
        
if __name__ == "__main__":
    ide = ide_config()
    
    ide.remove_folder(6)
    print ide.get_folders()
    #return
    #ide.set_folders([1,2,3,4])