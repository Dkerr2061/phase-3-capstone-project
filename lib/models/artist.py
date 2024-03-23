from models.__init__ import CONN, CURSOR
import colorama

class Artist:
    
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if( not hasattr(self, 'name')) and (isinstance(name_param, str)):
            self._name = name_param
        else:
            raise Exception('Artist name has to be a string and cannot be repeated.')
        
    def __repr__(self):
        return (colorama.Fore.LIGHTGREEN_EX + f"< Artist {self.id}: Name = {self.name} >")

    @classmethod
    def create_table(cls):
        pass
    
    @classmethod
    def drop_table(cls):
        pass
    
    def save(self):
        pass
    
    @classmethod
    def create(cls, name):
        pass
    
    @classmethod
    def instance_from_db(cls, row):
        pass
    
    @classmethod
    def get_all(cls):
        pass
    
    @classmethod
    def find_by_id(cls, id):
        pass
    
    @classmethod
    def find_by_name(cls, name):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def albums(self):
        pass