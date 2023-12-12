import os
import subprocess

class Games:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def startGameMode(self):
        """
        Starts the game mode where the user can select and play games.
        """
        self.run_game_mode()

    def run_game_mode(self):
        """
        Runs the game mode, allowing the user to select games and return to the main menu.
        """
        while True:
            print("\nSelect a game or type 'exit' to return to the main menu:")
            self.menuGames()
            print("Type the name of the game or 'exit':\n")
            game = input("--> ").lower()

            if game.lower() == 'exit':
                print("\n<EXIT GAME MODE>")

                break
            else:
                script_path = os.path.dirname(__file__)
                self.play_game(script_path + "\\" + self.dir_path + game)

    def menuGames(self):
        """
        Prints a list of games available for the user to select.
        """
        files = os.listdir(self.dir_path)

        print("")

        for file in files:
            if file == "Data":
                continue
            print(">-[ " + file + " ]-<")

        print("")

    def play_game(self, game):
        """
        Attempts to play the specified game.

        If the game is found, it will be started. If not, an error message will be displayed.
        """

        print("\n-----------------------------------------------------------------------------\n")

        try:
            # Running another script
            subprocess.run(["python", game])
        except FileNotFoundError:
            print("\nError: Game not found.\n")