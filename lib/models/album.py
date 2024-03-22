from models.__init__ import CONN, CURSOR

class Album:
    
    all = []

    def __init__(self, name, year, songs, id=None):
            self.name = name
            self.year = year
            self.songs = songs
            self.id = id
        