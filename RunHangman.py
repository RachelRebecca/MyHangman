import ComputerHangman
import TwoPlayerHangman
import PlayerClass


class RunProgram:
    hangMan = ComputerHangman.Hangman()
    twoPlayers = TwoPlayerHangman.TwoPlayers()
    run_player = PlayerClass.Player()

    def menu(self):
        print()
        print("----------------------------------------------------------------------")
        print("|                         MENU                                       |")
        print("|--------------------------------------------------------------------|")
        print("| 0.                  Quit program                                   |")
        print('|                                                                    |')
        print("| 1.   Play a new game of one person against the computer            |")
        print("| 2.        Play a new game against multiple players                 |")
        print('|                                                                    |')
        print("| 3.  Continue your old game of one person against the computer      |")
        print("| 4. Continue your old game of one person against multiple players   |")
        print("----------------------------------------------------------------------")
        print()
        choice = int(input("Enter the choice: "))
        while choice <0 or choice > 4:
            choice = int(input("Enter a valid choice: "))
        return choice

    def run(self):
        choice = -1
        while choice != 0:
            choice = self.menu()
            if choice == 1:
                RunProgram.hangMan.player.reset()
                RunProgram.hangMan.num_guesses = 10
                RunProgram.hangMan.guess_control = 10
                RunProgram.hangMan.name = "Player"
                RunProgram.hangMan.run()
            elif choice == 2:
                RunProgram.twoPlayers.reset()
                RunProgram.twoPlayers.num_guesses = 10
                RunProgram.twoPlayers.guess_control = 10
                RunProgram.twoPlayers.players = []
                RunProgram.twoPlayers.run()
            elif choice == 3:
                RunProgram.hangMan.num_guesses = RunProgram.hangMan.guess_control
                RunProgram.hangMan.run()
            elif choice == 4:
                RunProgram.twoPlayers.num_guesses = RunProgram.twoPlayers.guess_control
                RunProgram.twoPlayers.run()
        print("Thanks for playing!")


run = RunProgram()
run.run()