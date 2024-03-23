from models.__init__ import CONN, CURSOR

class Album:
    
  all = []

  def __init__(self, name, year, songs, id=None):
          self.name = name
          self.year = year
          self.songs = songs
          self.id = id

  @property
  def name(self):
        return self._name
  @name.setter
  def name(self, name_param):
        if(not hasattr(self, 'name')) and (isinstance(name_param, str)):
              self._name = name_param
        else:
              raise Exception('Album name has to be a string and cannot be repeated.')
        
  @property
  def year(self):
        return self._year
  @year.setter
  def year(self, year_param):
        if(isinstance(year_param, int)) and (1900 <= year_param <= 2024):
              self._year = year_param
        else:
              raise Exception('Year must be an integer between the years 1900 and 2024.')
        
  @property
  def songs(self):
        return self._songs
  @songs.setter
  def songs(self, songs_param):
        if(isinstance(songs_param, str)) and ( 1 <= len(songs_param) <= 40):
              self._songs = songs_param
        else:
              raise Exception('Song has to be a string between 1 to 40 characters.')