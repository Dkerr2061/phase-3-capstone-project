from models.__init__ import CONN, CURSOR
import colorama

class Album:
    
  all = []

  def __init__(self, name, year, songs, artist_id, id=None):
          self.name = name
          self.year = year
          self.songs = songs
          self.artist_id = artist_id
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
        
  @property
  def artist_id(self):
        return self._artist_id
  @artist_id.setter
  def artist_id(self, artist_id_param):
        if(isinstance(artist_id_param, int)):
              self._artist_id = artist_id_param
        else:
              raise Exception('Artist ID must be an Integer.')
        
  def __repr__(self):
        return (colorama.Fore.LIGHTGREEN_EX + f"< Album {self.id}: Name = {self.name}, Year = {self.year}, Songs = {self.songs}, Artist ID = {self.artist_id} >")
  
  @classmethod
  def create_table(cls):
        pass
  
  @classmethod
  def drop_table(cls):
        pass
  
  def save(self):
        pass
  
  @classmethod
  def create(cls, name, year, songs, artist_id):
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
  
  @classmethod
  def find_by_year(cls, year):
        pass
  
  def update(self):
        pass
  
  def delete(self):
        pass
  
  def artists(self):
        pass