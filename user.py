import json
import os



class User:
    def __init__(self, name):
        self.username = name
        self.balance = 1200
        self.wins = 0
        self.losses = 0

    def games_played(self):

        return self.wins + self.losses
    
    def win_rate(self):
        total=self.games_played()
        if total==0:

            return 0
        return (self.wins/total)*100
    


    def stats(self):
        
        print("------ Stats ------")
        print(f"Username: {self.username}")
        print(f"Balance: ₹{self.balance}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Games Played: {self.games_played()}")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount


    def save(self):
        data = {}

        
        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}

        
        data[self.username] = {
            "balance": self.balance,
            "wins": self.wins,
            "losses": self.losses
        }

        
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


    
    @classmethod
    def load(cls, name):
        if not os.path.exists("data.json"):
            return None

        with open("data.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return None

        if name in data:
            user_data = data[name]
            return cls(
                name,
                user_data["balance"],
                user_data["wins"],
                user_data["losses"]
            )

        return None

    
