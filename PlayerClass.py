class Player:
    def __init__(self):
        self.name = "Player"
        self.wins = 0
        self.losses = 0

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_wins_percent(self):

        total = self.get_wins() + self.get_losses()
        if total == 0:
            return format(0.00, ".2f")
        else:
            percent = format(round(((self.get_wins()/total) * 100), 2), ".2f")
            return percent

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_win(self):
        self.wins += 1

    def add_loss(self):
        self.losses += 1

    def reset(self):
        self.wins = 0
        self.losses = 0

    def __str__(self):
        return self.get_name() + "\n---------------------------" + \
               "\nwins: " + str(self.get_wins()) + "\nlosses: " + str(self.get_losses())

