from models.__init__ import CONN, CURSOR

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
