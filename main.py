from user import User
from games import DiceGame, GuessGame, BlackjackGame

def main():
    print("-------------------------")
    print("welcome to Casino games")
    name=input("Enter your name : ")
    game_user=User.load(name)
    if game_user:
        print("Welcome back!")
    else:
        print("New user created.")
    game_user = User(name)

    while True:
        print("\n------ Casino Menu ------")
        print("1. Dice Game")
        print("2. Guess Game")
        print("3. Blackjack")
        print("4. View Stats")
        print("5. Exit")
        print("6. Deposit Money")

        choice = int(input("Choose an option: "))

        match choice:
            case 1:
                game=DiceGame(game_user)
                game.play()
            
            case 2:
                game=GuessGame(game_user)
                game.play()

            case 3:
                game=BlackjackGame(game_user)
                game.play()

            case 4:
                game_user.stats()

            case 5:
                print("Exit !! Goodbye!!")
                game_user.save()
                break

            case 6:
                amount = int(input("Enter deposit amount: "))
                game_user.deposit(amount)

            
            case _:
                print("Wrong choice Try again ")

                
main()


        

    