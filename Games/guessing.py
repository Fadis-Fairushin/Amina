import random
from colorama import Fore, Style

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses_taken = 0

    def play(self):
        print("Welcome to the Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            guess = input("Take a guess: ")

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            self.guesses_taken += 1

            if guess < self.number:
                print(Fore.BLUE + "Too low!" + Style.RESET_ALL)
            elif guess > self.number:
                print(Fore.RED + "Too high!" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Congratulations! You guessed the number in {self.guesses_taken} tries." + Style.RESET_ALL)
                break

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
