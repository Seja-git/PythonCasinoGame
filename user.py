
class User:
    def __init__(self, name):
        self.username = name
        self.balance = 1200
        self.wins = 0
        self.losses = 0

    def stats(self):
        total_played = self.wins + self.losses
        print("------ Stats ------")
        print(f"Username: {self.username}")
        print(f"Balance: ₹{self.balance}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Games Played: {total_played}")
