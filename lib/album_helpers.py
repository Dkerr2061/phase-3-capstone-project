from models.album import Album
import colorama

def initialize_album_data():
    Album.create_table()
    Album.get_all()

def interact_with_album_data():
    print(colorama.Fore.LIGHTGREEN_EX + "You are interacting with the album data.")