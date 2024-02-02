import sys
import cracking
from colorama import Fore

def main(hash, file):
    try:
        return cracking.analyse_hash(hash, file)
    except FileNotFoundError:
        print(Fore.RED, "File not found\n", Fore.RESET)
        sys.exit(1)

if __name__ == '__main__':
    
    print(Fore.GREEN,   "||========================== WELCOME ===========================||\n", Fore.RESET)
    print(Fore.CYAN,    "||\t\tAuthor: WanisC - Language: Python                ||\n", Fore.RESET)
    print(Fore.CYAN,     "||\t\tVersion: 2024                                    ||\n", Fore.RESET)
    print(Fore.CYAN,    "||\t\t@Contact: https://github.com/WanisC              ||\n", Fore.RESET)
    print(Fore.GREEN,   "||======================== Gather Intel ========================||\n", Fore.RESET)

    user_target= input("\t\t\tEnter Your password: ")
    user_wordlist= input("\t\t\tEnter Your wordlist: ")
    print("\n")
    passwordcracked = main(user_target, user_wordlist)
    if passwordcracked:
        print(Fore.LIGHTBLACK_EX, "||========================== OUTPUT ===========================||\n", Fore.RESET)
        print(Fore.RED,  "\t\tYour password is ===> ", passwordcracked, "\n", Fore.RESET)
        print(Fore.LIGHTBLACK_EX, "||=============================================================||\n", Fore.RESET)
    else:
        print(Fore.LIGHTBLACK_EX, "||========================== OUTPUT ===========================||\n", Fore.RESET)
        print(Fore.RED,  "\t\tPassword not found\n", Fore.RESET)
        print(Fore.LIGHTBLACK_EX, "||=============================================================||\n", Fore.RESET)