class Together:
    def __init__(self):
        self.num_guesses = 10
        self.guess_control = 10

    def change_guesses(self):
        print("There are currently ", self.num_guesses, "guesses.")
        self.num_guesses = int(input("Enter the new number of guesses (number must not be less than 5): "))
        while self.num_guesses < 5:
            self.num_guesses = int(input("Enter a valid number of guesses (number must not be less than 5): "))
        self.guess_control = self.num_guesses
        print("There are now ", self.num_guesses, "guesses.")

