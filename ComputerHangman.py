import random
import linecache
import PlayerClass

class Hangman:

    def __init__(self):
        self.a = random.randint(1, 214)
        self.specLine = linecache.getline("HangmanWords.txt", self.a)
        self.charList = []
        self.player = PlayerClass.Player()
        self.name = "Player"
        self.num_guesses = 10
        self.guess_control = 10

    def welcome_message(self):
        print()
        print("\u001b[34mWelcome, \u001b[30m", self.player.get_name(),  ",\u001b[34m to Hangman!")
        print("A random word has been selected, "
              "and each letter is represented by a \"_\".")
        print("Keep guessing letters until you find the right word,"
              " or until you run out of guesses.")
        print("By default, you only get 10 wrong guesses before the game ends.")
        print("Choose your letters wisely. \u001b[0m")
        print()

    def get_word(self):
        self.a = random.randint(1, 214)
        self.specLine = linecache.getline("HangmanWords.txt", self.a)
        print("THE WORD: ")
        self.charList = []
        for i in range(1, len(self.specLine)):
            self.charList.append("_")

        for i in range(len(self.charList)):
            print(self.charList[i], end=" ")

        print("   (", len(self.charList), "letters)")
        print()

    def play_hangman(self):
        self.get_word()
        letter = "_"
        print("You have", self.num_guesses, "guesses left!")

        guess_list = []
        while (letter in self.charList) and (self.num_guesses <= self.guess_control):
            guess = input("Guess a letter: ")
            while guess in guess_list:
                print("You already guessed that one.")
                guess = input("Guess something else: ")
            guess_list.append(guess)

            if guess in self.specLine:
                for index in range(len(self.charList)):
                    if self.specLine[index] == guess:
                        self.charList[index] = guess

            else:
                self.num_guesses -= 1
                if self.num_guesses == 0:
                    print("Sorry, you ran out of guesses.")
                    print("The word was\u001b[31m", self.specLine, "\u001b[0m")
                    self.player.add_loss()
                    break

            for i in range(len(self.charList)):
                print(self.charList[i], end=" ")
            print()

            if letter not in self.charList:
                print()
                print("Congratulations! You guessed the word\u001b[33m", end=" ")
                for i in range(len(self.charList)):
                    print(self.charList[i], end="")
                print("\u001b[0m!! ")
                self.player.add_win()
                break

            else:
                print("You have", self.num_guesses, "guesses left!")
                print()

        self.num_guesses = self.guess_control

    def change_guesses(self):
        print("There are currently ", self.num_guesses, "guesses.")
        self.num_guesses = int(input("Enter the new number of guesses (number must not be less than 5): "))
        while self.num_guesses < 5:
            self.num_guesses = int(input("Enter a valid number of guesses (number must not be less than 5): "))
        self.guess_control = self.num_guesses
        print("There are now ", self.num_guesses, "guesses.")

    def set_player(self, name):
        self.player.set_name(name)

    def get_player(self):
        if self.name == "Player":
            self.name = input("Please enter your name: ")
            self.set_player(self.name)
            return self.player.get_name()

    def menu_choice(self):
        print()
        print("----------------------------------")
        print("|             Menu               |")
        print("|--------------------------------|")
        print("| 0.        End game             |")
        print("| 1. Display welcome message     |")
        print("| 2.       Play game             |")
        print("| 3.     Display stats           |")
        print("| 4.      Reset stats            |")
        print("| 5. Change number of guesses    |")
        print("----------------------------------")
        print()
        choice = int(input("Enter your choice from the menu: "))
        while choice < 0 or choice > 5:
            choice = int(input("Please enter a valid choice: "))
        return choice

    def run(self):
        self.get_player()
        choice = -1
        while choice != 0:
            choice = self.menu_choice()
            if choice == 1:
                print()
                self.welcome_message()
            elif choice == 2:
                print()
                self.play_hangman()
                print()
            elif choice == 3:
                print()
                print(self.player)
                print()
            elif choice == 4:
                print()
                self.player.reset()
                print(self.player)
                print()
            elif choice == 5:
                print()
                self.change_guesses()
                print()
        if choice == 0:
            print("wins percent: ", self.player.get_wins_percent(), "%")
            print("Good game, ", self.player.get_name(), end="")
            print("!")
