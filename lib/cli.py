# lib/cli.py
import colorama
import math
from helpers import (
    exit_program,
    helper_1
)

colorama.init()

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '■' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r[{bar}] {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r[{bar}] {percent:.2f}%", end="\r")

numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)


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
    print(colorama.Fore.RED + "Please select an option:")
    print(colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "0. Exit the program")
    print(colorama.Fore.BLUE + "1. Some useful function")
    print(colorama.Fore.RESET)



if __name__ == "__main__":
    main()
