from colorama import Fore, Style

def print_banner():
    print(open("banner.txt").read())

def ok(msg): print(Fore.GREEN + "[OK] " + msg + Style.RESET_ALL)
def warn(msg): print(Fore.YELLOW + "[!] " + msg + Style.RESET_ALL)
def bad(msg): print(Fore.RED + "[X] " + msg + Style.RESET_ALL)
def info(msg): print(Fore.CYAN + "[*] " + msg + Style.RESET_ALL)
