import socket
from colorama import *

PORT = 8080

def chatClient(IP):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    flag = True
    while flag:
        client.send(input("I: ").encode("utf-8"))
        msg = client.recv(1024).decode("utf-8")
        if msg == "quit":
            print(Fore.GREEN + "[ Exiting the chat and ending the program ]")
            flag = False
        else:
            print(Fore.CYAN + "_: " + msg)
    client.close()

def chatServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = socket.gethostbyname(socket.gethostname())
    print("Server address: " + IP)   
    server.bind((IP, PORT))
    server.listen()
    client, address = server.accept()
    flag = True
    while flag:
        msg = client.recv(1024).decode("utf-8")
        if msg == "quit":
            print(Fore.GREEN + "[ Shutting down the server and ending the program ]")
            flag = False
        else:
            print(Fore.CYAN + "_: " + msg)
        client.send(input("Server: ").encode("utf-8"))
    client.close()
    server.close()