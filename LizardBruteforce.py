import random, os, string, requests, threading, ctypes, easygui
from colorama import Fore
from time import sleep

proxy = set()
with open("proxies.txt", "r") as f:
    x = f.readlines()
    for line1 in x:
        proxy.add(line1.strip())
        
proxies = {
    'http': 'http://'+random.choice(list(proxy))
}

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2

    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def ui():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f"ANONFILES BRUTEFORCER | Made by @LizardX2 on Telegram") 
    font = """
             ▄▄▄·  ▐ ▄        ▐ ▄ ·▄▄▄      ▄▄▄   ▄▄· ▄▄▄ .▄▄▄  
            ▐█ ▀█ •█▌▐█▪     •█▌▐█▐▄▄·▪     ▀▄ █·▐█ ▌▪▀▄.▀·▀▄ █·
            ▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌██▪  ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄▐▀▀▄ 
            ▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌██▌.▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌▐█•█▌
             ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪▀▀▀  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ .▀  ▀"""
    faded = ''
    red = 50
    for line in font.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 125:
                red = 255
    print(center(faded))
    print(center(f'{Fore.LIGHTYELLOW_EX}\ngithub.com/LizardX2 Version 1.0\n{Fore.RESET}'))

def error():
    print(f"{Fore.RED}\n [!] ERROR! Something is wrong, aborting...{Fore.RESET}")
    exit()
    
def error_settings():
    print(f"{Fore.RED}\n [!] ERROR! Threads setting must be int...{Fore.RESET}")
    exit()
ui()
settings = input(f"{Fore.YELLOW}How many threads? > {Fore.RESET}")
try:
    settings = int(settings)
    pass
except:
    error_settings()

def bruteforce():
    clear()
    while True:
        random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 10))
        target = f"https://anonfiles.com/{random_string}"
        sent = requests.get(target, proxies=proxies, allow_redirects=True)
        if sent.status_code == 404:
            print(f"{Fore.RED}[-] {target}{Fore.RESET}")
            pass
        elif sent.status_code == 200:
            print(f"{Fore.GREEN}[+] FOUND! Saving {target}{Fore.RESET}")
            logs = open("valid.txt", "a")
            logs.write(target + "\n")
            logs.close
        else:
            error()

threads = []
for _ in range(settings):
    start = threading.Thread(target=bruteforce)
    start.daemon = True
    threads.append(start)

for _ in range(settings):
    threads[_].start()

for _ in range(settings):
    threads[_].join()