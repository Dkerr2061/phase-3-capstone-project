# lib/cli.py
import colorama

from load_bar import *
from artist_helpers import *
from album_helpers import *
    

def exit_program():
    print("Goodbye!")
    exit()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print(colorama.Fore.LIGHTRED_EX + "Please select an option:")
    print(colorama.Fore.RESET)
    print(colorama.Fore.LIGHTCYAN_EX + "1. Some useful function")
    print(colorama.Fore.LIGHTCYAN_EX + "0. Exit the program")
    print(colorama.Fore.RESET)
    



if __name__ == "__main__":
    main()
