from models.__init__ import CONN, CURSOR

class Artist:
    
    def __init__(self, name, id=None):
        self.name = name
        self.id = id
        