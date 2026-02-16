from user import User
from games import DiceGame, GuessGame, BlackjackGame

def main():
    print("-------------------------")
    print("welcome to Casino games")
    name=input("Enter your name : ")
    game_user=User(name)

    while True:
        print("\n------ Casino Menu ------")
        print("1. Dice Game")
        print("2. Guess Game")
        print("3. Blackjack")
        print("4. View Stats")
        print("5. Exit")

        choice = input("Choose an option: ")

        

    