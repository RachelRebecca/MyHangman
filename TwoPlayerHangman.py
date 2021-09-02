import PlayerClass


class TwoPlayers:
    def __init__(self):
        self.specLine = "Beautiful"
        self.charList = []
        self.players = []
        self.player1 = ' '
        self.num_guesses = 10
        self.guess_control = 10

    def welcome_message(self):
        if len(self.players) <= 1:
            self.add_players()
        print()
        print("\u001b[34mWelcome, \u001b[30m")
        for item in self.players:
            print(item.get_name(), end=", ")
        print("\u001b[34mto Hangman!")
        print("One of the players has chosen a word, "
              "and each letter is represented by a \"_\".")
        print("The rest of you will keep guessing letters in turns "
              "until you find the right word,"
              " or until you run out of guesses.")
        print("By default, you only get 10 wrong guesses before the game ends.")
        print("Choose your letters wisely. \u001b[0m")
        print()

    def get_word(self):
        self.specLine = input(self.player1.get_name() + ", please enter your word: ").lower().strip()
        while len(self.specLine) < 3:
            self.specLine = input(self.player1.get_name() + ", please enter a valid word: ").lower().strip()
        print("\n" * 35)
        print("THE WORD: ")
        self.charList = []
        for i in range(len(self.specLine)):
            self.charList.append("_")

        for i in range(len(self.charList)):
            print(self.charList[i], end=" ")

        print("   (", len(self.charList), "letters)")
        print()

    def play_hangman(self):
        while len(self.players) <= 1:
            print("You don't have enough players.")
            self.add_players()

        for index in range(len(self.players)):
            print((index+1), ": ", self.players[index].get_name())

        player_index = int(input("Enter the number of the player who will make the words: "))
        self.player1 = self.players[player_index - 1]

        self.get_word()
        letter = "_"
        player_indexes = 0
        print("You have", self.num_guesses, "guesses left!")

        guess_list = []
        while (letter in self.charList) and (self.num_guesses <= self.guess_control):
            if self.players.index(self.players[player_indexes]) == self.players.index(self.player1):
                if self.players.index(self.player1) == 0:
                    player_indexes += 1
                else:
                    player_indexes = 0

            guess = input(self.players[player_indexes].get_name() + ", guess a letter: ").lower().strip()
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
                    self.player1.add_win()
                    for index in range(0, len(self.players)):
                        if index != self.players.index(self.player1):
                            self.players[index].add_loss()
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
                self.player1.add_loss()
                for index in range(0, len(self.players)):
                    if index != self.players.index(self.player1):
                        self.players[index].add_win()
                break

            else:
                print("You have", self.num_guesses, "guesses left!")
                if (player_indexes + 1) < len(self.players):
                    if self.players.index(self.players[player_indexes + 1]) == self.players.index(self.player1):
                        if (player_indexes + 2) < len(self.players):
                            player_indexes += 1
                        else:
                            player_indexes = 0
                    player_indexes += 1
                else:
                    player_indexes = 0
                print()
        self.num_guesses = self.guess_control

    def change_guesses(self):
        print("There are currently ", self.num_guesses, "guesses.")
        self.num_guesses = int(input("Enter the new number of guesses (number must not be less than 5): "))
        while self.num_guesses < 5:
            self.num_guesses = int(input("Enter a valid number of guesses (number must not be less than 5): "))
        self.guess_control = self.num_guesses
        print("There are now ", self.num_guesses, "guesses.")

    def add_players(self):
        name = input("Enter name of new player: ")
        new_player = PlayerClass.Player()
        self.players.append(new_player)
        new_player.set_name(name)
        if len(self.players) == 1:
            self.add_players()

    def display_stats(self):
        if len(self.players) == 0:
            print("You don't have any players.")
            print("Make sure to add some soon! :)")
        for item in self.players:
            print(item, end="\n\n")

    def reset(self):
        for item in self.players:
            item.reset()

    def leaderboard(self):
        if len(self.players) == 0:
            print("You don't have any players.")
            print("Make sure to make some soon! :)")
            return ' '
        best_ten = sorted(self.players, key=lambda x: x.get_wins_percent(), reverse=True)
        if len(best_ten) > 10:
            for item in best_ten[:10]:
                print("Player name : ", format(item.get_name(), '<20s'), format("Player win percentage : ", '>30s'), item.get_wins_percent())
        else:
            for item in best_ten:
                print("Player name : ", format(item.get_name(), '<20s'), format("Player win percentage : ", '>30s'), item.get_wins_percent())
        return ''

    def menu_choice(self):
        print()
        print("------------------------------------------")
        print("|               Menu                     |")
        print("|----------------------------------------|")
        print("| 0.           End game                  |")
        print("| 1.     Display welcome message         |")
        print("| 2.          Play game                  |")
        print("| 3.        Display stats                |")
        print("| 4.         Reset stats                 |")
        print("| 5.         Add a player                |")
        print("| 6.      Display leaderboard            |")
        print("| 7.   Change number of guesses          |")
        print("------------------------------------------")

        print()
        choice = int(input("Enter your choice from the menu: "))
        while choice < 0 or choice > 7:
            choice = int(input("Please enter a valid choice: "))
        return choice

    def run(self):
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
                self.display_stats()
                print()
            elif choice == 4:
                print()
                self.reset()
                self.display_stats()
                print()
            elif choice == 5:
                print()
                self.add_players()
                print()
            elif choice == 6:
                print()
                self.leaderboard()
                print()
            elif choice == 7:
                print()
                self.change_guesses()
                print()
        if choice == 0:
            print("Good game!")
