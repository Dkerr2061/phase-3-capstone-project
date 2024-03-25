# lib/helpers.py
from models.artist import Artist
import colorama

def initialize_artist_data():
    Artist.create_table()

    Artist.get_all()


def interact_with_artist_data():
    print(colorama.Fore.LIGHTGREEN_EX + "You are interacting with the artist data.")
    while True:
        artist_menu()
        user_input = input("Select and option: ")
        if(user_input == 'a'):
             retrieve_all_artists()
             break
        elif (user_input == 'c'):
             print("Enter new artists name: ")
             break
        elif (user_input == 'u'):
             print("Enter the ID for the artist to update: ")
             break
        elif (user_input == 'd'):
             print("Delete artist")
             break
        else:
             print(colorama.Fore.RED + 'Invalid input, please try again.')
             print(colorama.Fore.RESET)
            


def artist_menu():
        print("\nPress A to search artists")
        print("Press C to create artist")
        print("Press U to update artist")
        print("Press D to delete artist\n")

        
def retrieve_all_artists():
     artist_search_options()
     user_input = input("Select option: ")
     while True:
        if(user_input == 'a'):
            for artist in Artist.get_all():
                print(artist)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == 'i'):
            while True:
                try:
                    user_input = input("\nEnter the id number for the artist: ")
                    user_input = int(user_input)
                    artist = Artist.find_by_id(user_input)
                    if(artist):
                        print("\nHere is the artist that matched the entered id:")
                        print(Artist.find_by_id(user_input))
                    else:
                            print("\nArtist not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                        print("Invalid input, please try again.")
            break
        elif(user_input == 'n'):
            while True:
                try:
                    user_input = input("Enter artist's name: ")
                    user_input = str(user_input)
                    artist = Artist.find_by_name(user_input)
                    if(artist):
                         print("\nHere are the artist's that match that name:")
                         print(Artist.find_by_name(user_input))
                    else:
                         print("No artist waas found with that name.")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                     print("Invalid input, please try again.")
            break


def artist_search_options():
     print("\nWould you like to see all or search by ID or Name?")
     print("a: To see all artist's.")
     print("i: To search by id.")
     print("n: To search by name.\n")