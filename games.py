
import random

class CasinoGame:
    
    def __init__(self, user):
        self.user = user
        self.bet = 0

    def place_bet(self):
        self.bet = int(input("Place your bet amount: "))
        
        if self.bet > 0 and self.bet <= self.user.balance:
            self.user.balance -= self.bet
        else:
            print("Invalid bet amount.")
            self.bet = 0

    def win(self, amount_mul):
        winnings = self.bet * amount_mul
        self.user.balance += winnings
        self.user.wins += 1
       
        print(f"You won ₹{winnings}!")

    def loss(self):
        self.user.losses += 1
       
        print("You lost the bet.")


class DiceGame(CasinoGame):
    
    def play(self):
        self.place_bet()
        
        if self.bet == 0:
            return
        
        number = int(input("Choose a number (1-6): "))
        dice = random.randint(1, 6)
        
        print("Dice rolled:", dice)
        
        if number == dice:
            self.win(2)
        else:
            self.loss()

class GuessGame(CasinoGame):
    
    def play(self):
        self.place_bet()
        
        if self.bet == 0:
            return
        
        number = int(input("Choose a number (1-10): "))
        ran_num = random.randint(1, 10)
        
        print("Random number is :", ran_num)
        
        if number == ran_num:
            self.win(2)
        else:
            self.loss()

class BlackjackGame(CasinoGame):
    
    def play(self):
        self.place_bet()
        
        if self.bet == 0:
            return
        

        Pcard1=random.randint(1,11)
        Pcard2=random.randint(1,11)
        Psum=Pcard1+Pcard2
        Dcard1=random.randint(1,11)
        Dcard2=random.randint(1,11)
        Dsum=Dcard1+Dcard2

        print(f"Player cards: {Pcard1}, {Pcard2} (Total: {Psum})")
        print(f"Dealer cards: {Dcard1}, {Dcard2} (Total: {Dsum})")


        if Psum >21:
            self.loss()
            return
        
        if Dsum >21:
            self.win(2)
            return
        
        if Psum>Dsum:
            self.win(2)
        elif Psum<Dsum:
            self.loss()
        else:
            self.user.balance += self.bet
            print("It's a tie! Bet refunded.")
            



