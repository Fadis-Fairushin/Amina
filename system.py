from textInterface import cls_clear
from colorama import *

init(autoreset = True)

def startSystem():
    cls_clear(100)
    print('----------------')
    print('[ START SYSTEM ]')
    print('----------------')
    print(Fore.GREEN + '\n[ The system is ready to work ]')