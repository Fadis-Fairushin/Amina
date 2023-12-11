import os
from datetime import datetime
import socket
from threading import Thread
from colorama import *
from hacker import portScanner
from utils import cursorPosition
from chat import chatClient, chatServer
from guiInterface import Gui

__dir__ = "User\\"
__cd__ = ""

init(autoreset = True)

def scanner(command=""):
    global __dir__, __cd__
    if command == "":
        command = input("\n>>> ").lower()
    if command == "help":
        print("Commands for system management:")
        print(Fore.BLUE + "HELP" + Fore.WHITE + " - List of all commands")
        print(Fore.BLUE + "EXIT" + Fore.WHITE + " - Turn off the system")
        print(Fore.BLUE + "PRINT" + Fore.WHITE + " - Print the text following the command")
        print(Fore.BLUE + "CLS or CLEAR" + Fore.WHITE + " - Clear the console")
        print(Fore.BLUE + "SYSTEMINFO" + Fore.WHITE + " - Information about the system")
        print(Fore.BLUE + "CF <FILE_NAME>" + Fore.WHITE + " - Creates a file")
        print(Fore.BLUE + "RENAME <FILE_NAME> <NEW_FILE_NAME>" + Fore.WHITE + " - Renames the file")
        print(Fore.BLUE + "DEL <FILE_NAME>" + Fore.WHITE + " - Deletes the file")
        print(Fore.BLUE + "CAT <FILE_NAME>" + Fore.WHITE + " - Display the contents of the file")
        print(Fore.BLUE + "INSERT <FILE_NAME>" + Fore.WHITE + " - Insert text into a file")
        print(Fore.BLUE + "REPLACE <FILE_NAME>" + Fore.WHITE + " - Replace the text in the file")
        # Замена символов в файле
        print(Fore.BLUE + "MKDIR or MD" + Fore.WHITE + " - Creates a folder")
        print(Fore.BLUE + "RMDIR or RD" + Fore.WHITE + " - Deletes a folder")
        print(Fore.BLUE + "DIR or LS" + Fore.WHITE + " - Displays the contents of the directory")
        print(Fore.BLUE + "CD <FOLDER>" + Fore.WHITE + " - Moves you to the selected directory")
        print(Fore.BLUE + "CD .." + Fore.WHITE + " - Moves you up a level")
        print(Fore.BLUE + "CD ." + Fore.WHITE + " - Moves you to the home directory")
        print(Fore.BLUE + "DATETIME" + Fore.WHITE + " - Get the date and time")
        print(Fore.BLUE + "PORTSCANNER" + Fore.WHITE + " - Port Scanner: portScanner ip <number_of_ports>")
        print(Fore.BLUE + "CP" + Fore.WHITE + " - Shows the cursor position and the color of the pixel below it")
        print(Fore.BLUE + "chatServer" + Fore.WHITE + " - Starts the chat server and displays information about the server")
        print(Fore.BLUE + "chatClient" + Fore.WHITE + " - Launches the chat client and connects to the server")
    elif command == "exit":
        print("[ Exit ]")
        exit()
    elif command.find("print") != -1:
        command = command.replace("print", "")
        print(Fore.YELLOW + command.strip())
    elif ((command == "cls") or (command == "clear")):
        cls_clear(100)
    elif command == "systeminfo":
        print(Fore.GREEN + "The system is based on the Python programming language")
    elif command.find("cf") != -1:
        name_file = command.replace("cf", "")
        name_file_strip = name_file.strip()
        f_ = __dir__ + name_file_strip
        try:
            with open(f_, "w") as f:
                print(Fore.GREEN + "[ File " + name_file_strip + " created ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - You didn't specify the file name")
    elif command.find("rename") != -1:
        f_ = command.split(" ")
        try:
            f_old = __dir__ + f_[1]
            f_new = __dir__ + f_[2]
            os.rename(f_old, f_new)
            print(Fore.GREEN + "[ The file was renamed from " + f_old.replace(__dir__, "") + " on " + f_new.replace(__dir__, "") + " ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - So far, the system cannot rename files with spaces in the name")
            print(Fore.GREEN + "[ Error ] - Or you didn't specify the file name")
    elif command.find("del") != -1:
        f_ = command.split(" ")
        try:
            f_del = __dir__ + f_[1]
            os.remove(f_del)
            print(Fore.GREEN + "[ File " + f_[1] + " deleted ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - So far, the system cannot delete files with spaces in the name")
            print(Fore.GREEN + "[ Error ] - Or you didn't specify the file name")
    elif command.find("cat") != -1:
        f_ = command.split(" ")
        try:
            f_cat = __dir__ + f_[1]
            print(Fore.GREEN + "[ The contents of the file " + f_[1] + " ]")
            with open(f_cat, "r") as f:
                print(f.read())
        except Exception:
            print(Fore.GREEN + "[ Error ] - So far, the system cannot delete files with spaces in the name")
            print(Fore.GREEN + "[ Error ] - Or you didn't specify the file name")
    elif command.find("insert") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ If there was a space in the file name, a new file will be created with the name before the space. I am aware of this problem, but I have not solved it yet. ]")
            print(Fore.GREEN + "[ I set a limit of 10,000 lines, so when the limit is reached, save the file and open it again, otherwise data loss is possible! ]")
            print(Fore.GREEN + "[ To save and exit, type \"[save]\" without quotes on a separate line ]")
            print(Fore.GREEN + "[ To exit without saving, type \"[exit]\" without quotes on a separate line ]")
            cls_clear(3)
            with open(f_ins, "a") as f:
                text = ""
                for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        f.write(f"\n\n\nДата: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ The file has been updated ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ The changes  not saved ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Error ] - You did not specify the file name")
    elif command.find("replace") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ If there was a space in the file name, a new file will be created with the name before the space. I am aware of this problem, but I have not solved it yet. ]")
            print(Fore.GREEN + "[ I set a limit of 10,000 lines, so when the limit is reached, save the file and open it again, otherwise data loss is possible! ]")
            print(Fore.GREEN + "[ To save and exit, type \"[save]\" without quotes on a separate line ]")
            print(Fore.GREEN + "[ To exit without saving, type \"[exit]\" without quotes on a separate line ]")
            cls_clear(3)
            text = ""
            for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        with open(f_ins, "w") as f:
                            f.write(f"Date: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ The file has been updated ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ The changes not saved ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Error ] - You did not specify the file name")
    elif ((command.find("rmdir") != -1) or (command.find("rd") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.rmdir(d_)
            print(Fore.GREEN + "[ The directory has been deleted ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - While the system cannot read files with spaces in the name")
            print(Fore.GREEN + "[ Error ] - Or you did not specify the file name")
    elif ((command.find("mkdir") != -1) or (command.find("md") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.mkdir(d_)
            print(Fore.GREEN + "[ The catalog has been created ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - While the system cannot read files with spaces in the name")
            print(Fore.GREEN + "[ Error ] - Or you did not specify the file name")
    elif ((command.find("ls") != -1) or (command.find("dir") != -1)):
        try:
            rez = sorted(os.listdir(__dir__))
            for n, item in enumerate(rez):
                #print(n+1, item)
                if item.find(".") != -1:
                    print("File:    ", item)
                else:
                    print("Folder: ", Fore.GREEN + item)
        except Exception:
            print(Fore.GREEN + "[ Error ] - There is no such directory, go up a level")
    elif command == "cd ..":
        __dir__ = __dir__.replace(__cd__, "")
        length = len(__cd__)
        print(Fore.GREEN + "[ You have logged out of the catalog " + __cd__[:length-1] + "and moved to a higher level]")
        __cd__ = ""
    elif command == "cd .":
        __dir__ = "User\\"
    elif command.find("cd") != -1:
        try:
            cd_ = command.split(" ")
            __cd__ += cd_[1] + "\\"
            __dir__ += __cd__
            print(Fore.GREEN + "[ You have moved to the catalog " + cd_[1] + " ]")
        except Exception:
            print(Fore.RED + "You didn't specify the catalog!")
    elif command == "datetime":
        d, t = dateAndTime()
        print(Fore.CYAN + "Date: " + d)
        print(Fore.CYAN + "Time: " + t)
    elif command.find("portscanner") != -1:
        try:
            start = datetime.now()
            ip = command.split(" ")
            if len(ip) == 3:
                if (int(ip[2]) > 65535) or (int(ip[2]) <= 0):
                    print(Fore.RED + "Ports are specified out of range")
                else:
                    for i in range(int(ip[2])):
                        potoc = Thread(target=portScanner, args=(ip[1], i))
                        potoc.start()
            elif len(ip) == 2:
                for i in range(int(65535)):
                    potoc = Thread(target=portScanner, args=(ip[1], i))
                    potoc.start()
            else:
                pass
            ends = datetime.now()
            print(Fore.GREEN + "Time : {}".format(ends-start))
        except Exception:
            print(Fore.RED + "You have not entered an ip address!")
    elif command == "cp":
        print("Press CTRL-C to quit")
        try:
            while True:
                cursorPosition()
        # When the user presses CTRL-C, an exception will occur KeyboardInterrupt
        except KeyboardInterrupt:
            print("\nExiting the program")
    elif command == "chatserver":
        chatServer()
    elif command.find("chatclient") != -1:
        try:
            IP = command.split(" ")
            chatClient(IP[1])
        except Exception:
            print(Fore.RED + "You have not entered an ip address!")
    elif command == "gui":
        try:
            pass
            #Gui()
        except Exception:
            pass
    else:
        print(Fore.BLUE + "[ The command was not recognized ]")

def cls_clear(num):
    for i in range(num):
        print()

def dateAndTime():
    d = datetime.today().strftime("%d.%m.%Y")
    t = datetime.today().strftime("%H:%M:%S")
    return d, t