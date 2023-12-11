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
        print("Команды для управления системой:")
        print(Fore.BLUE + "HELP" + Fore.WHITE + " - Список всех команд")
        print(Fore.BLUE + "EXIT" + Fore.WHITE + " - Выключить систему")
        print(Fore.BLUE + "PRINT" + Fore.WHITE + " - Вывести текст идущий после команды")
        print(Fore.BLUE + "CLS или CLEAR" + Fore.WHITE + " - Очистить консоль")
        print(Fore.BLUE + "SYSTEMINFO" + Fore.WHITE + " - Информация о системе")
        print(Fore.BLUE + "CF НАЗВАНИЕ_ФАЙЛА" + Fore.WHITE + " - Создает файл")
        print(Fore.BLUE + "RENAME НАЗВАНИЕ_ФАЙЛА НОВОЕ_НАЗВАНИЕ" + Fore.WHITE + " - Переименовывает файл")
        print(Fore.BLUE + "DEL НАЗВАНИЕ_ФАЙЛА" + Fore.WHITE + " - Удаляет файл")
        print(Fore.BLUE + "CAT НАЗВАНИЕ_ФАЙЛА" + Fore.WHITE + " - Отобразить содержимое файла")
        print(Fore.BLUE + "INSERT НАЗВАНИЕ_ФАЙЛА" + Fore.WHITE + " - Вставить текст в файл")
        print(Fore.BLUE + "REPLACE НАЗВАНИЕ_ФАЙЛА" + Fore.WHITE + " - Заменить текст в файле")
        # Замена символов в файле
        print(Fore.BLUE + "MKDIR или MD" + Fore.WHITE + " - Создает каталог")
        print(Fore.BLUE + "RMDIR или RD" + Fore.WHITE + " - Удаляет каталог")
        print(Fore.BLUE + "DIR или LS" + Fore.WHITE + " - Выводит содержимое каталога")
        print(Fore.BLUE + "CD КАТАЛОГ" + Fore.WHITE + " - Перемещает вас в выбранный каталог")
        print(Fore.BLUE + "CD .." + Fore.WHITE + " - Перемещает вас на уровень выше")
        print(Fore.BLUE + "CD ." + Fore.WHITE + " - Перемещает вас в домашний каталог")
        print(Fore.BLUE + "DATETIME" + Fore.WHITE + " - Получить дату и время")
        print(Fore.BLUE + "PORTSCANNER" + Fore.WHITE + " - Сканер портов: portScanner ip [количество портов]]")
        print(Fore.BLUE + "CP" + Fore.WHITE + " - Показывает позицию курсора и цвет пикселя под ним")
        print(Fore.BLUE + "chatServer" + Fore.WHITE + " - Запускает сервер чата и выводить информацию о сервере")
        print(Fore.BLUE + "chatClient" + Fore.WHITE + " - Запускает клиента чата и подкючается к серверу")
    elif command == "exit":
        print("[ Выход из системы ]")
        exit()
    elif command.find("print") != -1:
        command = command.replace("print", "")
        print(Fore.YELLOW + command.strip())
    elif ((command == "cls") or (command == "clear")):
        cls_clear(100)
    elif command == "systeminfo":
        print(Fore.GREEN + "Система на языке программирования Python")
    elif command.find("cf") != -1:
        name_file = command.replace("cf", "")
        name_file_strip = name_file.strip()
        f_ = __dir__ + name_file_strip
        try:
            with open(f_, "w") as f:
                print(Fore.GREEN + "[ Файл " + name_file_strip + " создан ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - Вы не указали название файла")
    elif command.find("rename") != -1:
        f_ = command.split(" ")
        try:
            f_old = __dir__ + f_[1]
            f_new = __dir__ + f_[2]
            os.rename(f_old, f_new)
            print(Fore.GREEN + "[ Файл переименован с " + f_old.replace(__dir__, "") + " на " + f_new.replace(__dir__, "") + " ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - Пока система не может переименовывать файлы имующие пробелы в название")
            print(Fore.GREEN + "[ Error ] - Или вы не указали название файла")
    elif command.find("del") != -1:
        f_ = command.split(" ")
        try:
            f_del = __dir__ + f_[1]
            os.remove(f_del)
            print(Fore.GREEN + "[ Файл " + f_[1] + " удален ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - Пока система не может удалять файлы имующие пробелы в название")
            print(Fore.GREEN + "[ Error ] - Или вы не указали название файла")
    elif command.find("cat") != -1:
        f_ = command.split(" ")
        try:
            f_cat = __dir__ + f_[1]
            print(Fore.GREEN + "[ Содержимое файла " + f_[1] + " ]")
            with open(f_cat, "r") as f:
                print(f.read())
        except Exception:
            print(Fore.GREEN + "[ Error ] - Пока система не может читать файлы имующие пробелы в название")
            print(Fore.GREEN + "[ Error ] - Или вы не указали название файла")
    elif command.find("insert") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ Если в название файла был пробел, то будет создан новый файл с названием до пробела. Я знаю об этой проблеме, но пока её не решил ]")
            print(Fore.GREEN + "[ Поставил лимит на 10 000 строк, поэтому при достижении предела сохраните файл и снова откройте, иначе возможно потеря данных! ]")
            print(Fore.GREEN + "[ Чтобы сохранить и выйти введите \"[save]\" без кавычек на отдельной строке ]")
            print(Fore.GREEN + "[ Чтобы выйти без сохранения введите \"[exit]\" без кавычек на отдельной строке ]")
            cls_clear(3)
            with open(f_ins, "a") as f:
                text = ""
                for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        f.write(f"\n\n\nДата: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ Файл обновлен ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ Изменения не сохранены ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Error ] - Вы не указали название файла")
    elif command.find("replace") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ Если в название файла был пробел, то будет создан новый файл с названием до пробела. Я знаю об этой проблеме, но пока её не решил! ]")
            print(Fore.GREEN + "[ Поставил пока лимит на 10 000 строк, поэтому при достижении предела сохраните файл и снова откройте, иначе возможно потеря данных! ]")
            print(Fore.GREEN + "[ Чтобы сохранить и выйти введите \"[save]\" без кавычек на отдельной строке ]")
            print(Fore.GREEN + "[ Чтобы выйти без сохранения введите \"[exit]\" без кавычек на отдельной строке ]")
            cls_clear(3)
            text = ""
            for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        with open(f_ins, "w") as f:
                            f.write(f"Дата: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ Файл обновлен ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ Изменения не сохранены ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Error ] - Вы не указали название файла")
    elif ((command.find("rmdir") != -1) or (command.find("rd") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.rmdir(d_)
            print(Fore.GREEN + "[ Каталог удален ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - Пока система не может читать файлы имующие пробелы в название")
            print(Fore.GREEN + "[ Error ] - Или вы не указали название файла")
    elif ((command.find("mkdir") != -1) or (command.find("md") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.mkdir(d_)
            print(Fore.GREEN + "[ Каталог создан ]")
        except Exception:
            print(Fore.GREEN + "[ Error ] - Пока система не может читать файлы имующие пробелы в название")
            print(Fore.GREEN + "[ Error ] - Или вы не указали название файла")
    elif ((command.find("ls") != -1) or (command.find("dir") != -1)):
        try:
            rez = sorted(os.listdir(__dir__))
            for n, item in enumerate(rez):
                #print(n+1, item)
                if item.find(".") != -1:
                    print("Файл:    ", item)
                else:
                    print("Каталог: ", Fore.GREEN + item)
        except Exception:
            print(Fore.GREEN + "[ Error ] - Такой деректории не существует, поднимитесь на уровень выше")
    elif command == "cd ..":
        __dir__ = __dir__.replace(__cd__, "")
        length = len(__cd__)
        print(Fore.GREEN + "[ Вы вышли из каталога " + __cd__[:length-1] + " и перешли на уровень выше ]")
        __cd__ = ""
    elif command == "cd .":
        __dir__ = "User\\"
    elif command.find("cd") != -1:
        try:
            cd_ = command.split(" ")
            __cd__ += cd_[1] + "\\"
            __dir__ += __cd__
            print(Fore.GREEN + "[ Вы перешли в каталог " + cd_[1] + " ]")
        except Exception:
            print(Fore.RED + "Вы не указали каталог!")
    elif command == "datetime":
        d, t = dateAndTime()
        print(Fore.CYAN + "Дата: " + d)
        print(Fore.CYAN + "Время: " + t)
    elif command.find("portscanner") != -1:
        try:
            start = datetime.now()
            ip = command.split(" ")
            if len(ip) == 3:
                if (int(ip[2]) > 65535) or (int(ip[2]) <= 0):
                    print(Fore.RED + "Порты указаны вне диапазона")
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
            print(Fore.RED + "Вы не ввели ip адрес!")
    elif command == "cp":
        print("Press CTRL-C to quit")
        try:
            while True:
                cursorPosition()
        # Когда пользователь нажмет CTRL-C, возникнет исключение KeyboardInterrupt
        except KeyboardInterrupt:
            print("\nExiting the program")
    elif command == "chatserver":
        chatServer()
    elif command.find("chatclient") != -1:
        try:
            IP = command.split(" ")
            chatClient(IP[1])
        except Exception:
            print(Fore.RED + "Вы не ввели ip адрес!")
    elif command == "gui":
        try:
            pass
            #Gui()
        except Exception:
            pass
    else:
        print(Fore.BLUE + "[ Команда не распознана ]")

def cls_clear(num):
    for i in range(num):
        print()

def dateAndTime():
    d = datetime.today().strftime("%d.%m.%Y")
    t = datetime.today().strftime("%H:%M:%S")
    return d, t