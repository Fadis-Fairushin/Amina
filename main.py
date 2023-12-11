from system import startSystem
from textInterface import scanner

def App():
    startSystem()
    try:
        while True:
            scanner()
    except KeyboardInterrupt:
        print("Ctrl+C")
        print("\n[ Exit ]")

if __name__ == "__main__":
    App()