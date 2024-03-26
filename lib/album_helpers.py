from models.album import Album
import colorama

def initialize_album_data():
    Album.create_table()
    Album.get_all()

def interact_with_album_data():
    print(colorama.Fore.LIGHTYELLOW_EX + "You are interacting with the album data.")
    while True:
        album_menu()
        user_input = input("Please select one of the following options:")
        if(user_input == 'a'):
            search_for_album()
            break
        elif(user_input == 'c'):
            print("this is to crate a new album")
            break
        elif(user_input == 'u'):
            print("this is to update an album")
            break
        elif(user_input == 'ar'):
            print("this is to get artist data")
            break
        elif(user_input == 'd'):
            print("this is used to delete an album")
            break
        else:
            print("Invalid input, please try again.")


def album_menu():
    print("\nEnter A to search for album:")
    print("Enter C to create a new album:")
    print("Enter U to update an existing album:")
    print("Enter AR to get the album's artist information:")
    print("Enter D to delete album\n")

def search_for_album_menu():
    print("\nChoose one of the following options:")
    print("Press A to get all albums:")
    print("Press I to search by id:")
    print("Press Y to search by year:\n")

def search_for_album():
    search_for_album_menu()
    user_input = input("Please choose option:")
    while True:
        if(user_input == 'a'):
            for album in Album.all:
                print(album)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == 'i'):
            while True:
                try:
                    user_input = input("\nEnter the album's ID: ")
                    user_input = int(user_input)
                    album = Album.find_by_id(user_input)
                    if(album):
                        print("\nHere is the album that matched the entered id:")
                        print(Album.find_by_id(user_input))
                    else:
                            print("\nAlbum not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    print("\n Invalid input, please try again.")
            break
        elif(user_input == 'y'):
            while True:
                try:
                    user_input = input("\nEnter album's release year: ")
                    user_input = int(user_input)
                    year = Album.find_by_year(user_input)
                    if(year):
                        print("\nHere is the album that matched the entered year:")
                        print(Album.find_by_year(user_input))
                    else:
                        print("\nAlbum not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    print("\n Invalid input, please try again.")
            break
