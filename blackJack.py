import random

class Deck(object):
    def __init__(self):
        self.listOfNumbers = ["Ace", "2", "3",  "4", "5", "6", "7", "8", "9", "10", "The Jack", "The Queen", "The King"]  
        self.listOfSuits = ["Clubs", "Hearts", "Spades", "Diamonds"]  
    def __str__(self):
        rep = random.choice(self.listOfNumbers) + " of " + random.choice(self.listOfSuits)
        return rep

class Player (object):
    
    def __init__(self):
        deck = Deck()
        self.card1 = str(deck)
        self.usedCards = []
        self.message = "This card is " + str(self.card1)
    def __str__(self):
        return self.message
    def checking (self):
        while True:
            for mess in self.usedCards:
                if message == mess:
                    message = "This card is " + self.card1
                    Player.checking()
                else: 
                    self.usedCards.append(message)
                   


class Dealer (object):
    def __init__ (self):
        self.answer = ""
    
    def dealerDecision(self, myCards):
        turn = Turn()
        player = Player()
        self.playerValue = myCards
        self.dealerValue = 0
        while self.dealerValue < self.playerValue:
            newPlayer = Player()            
            if len(newPlayer.card1.split(' ')[1]) >= 4:
                self.newValue = 10
            elif len(newPlayer.card1.split(' ')[0]) == 3:
                    if self.dealerValue <= 10:
                        self.newValue = 11
                    else:
                        self.newValue = 1
            else:
                self.newValue = int(newPlayer.card1.split(' ')[0]) 
            self.dealerValue = self.dealerValue + self.newValue
            print(newPlayer)
            print(self.dealerValue)
            if self.dealerValue > 21:   
                self.dealerValue = 0
                return "You Win"
            elif self.dealerValue >= self.playerValue:
                self.dealerValue = 0
                return "You Lose"
                
                
    def __str__ (self):
        self.answer = Dealer.dealerDecision
        return self.answer 
            
        
class Turn (object):
    def __init__(self):
        self.totalValue = 0
    
                     
    def playerDecision(self):
        newPlayer = Player()
        if len(newPlayer.card1.split(' ')[1]) >= 4:
            value1 = 10
            self.totalValue = self.totalValue + value1
        elif len(newPlayer.card1.split(' ')[0]) == 3:
                print(newPlayer)
                value1 = int(input("Should your ace be 1 or 11? "))   
                self.totalValue = self.totalValue + value1     
        else:
            value1 = int(newPlayer.card1.split(' ') [0])
            self.totalValue = self.totalValue + value1

        print(newPlayer)
        print(self.totalValue)
        newPlayer = Player()
        if len(newPlayer.card1.split(' ')[1]) >= 4:
            value1 = 10
            self.totalValue = self.totalValue + value1
        elif len(newPlayer.card1.split(' ')[0]) == 3:
            print(newPlayer)
            value1 = int(input("Should your ace be 1 or 11? "))   
            self.totalValue = self.totalValue + value1   
            
                
        else:
            value1 = int(newPlayer.card1.split(' ') [0])
            self.totalValue = self.totalValue + value1

        print(newPlayer)
        print(self.totalValue)
        
        while True:
            decision = input("Hit or Check? ").lower() 
            if decision == "check":
                total = self.totalValue
                self.totalValue = 0
                return total

            newPlayer = Player()
            if len(newPlayer.card1.split(' ')[1]) >= 4:
                value1 = 10
                self.totalValue = self.totalValue + value1
            elif len(newPlayer.card1.split(' ')[0]) == 3:
                print(newPlayer)
                value1 = int(input("Should your ace be 1 or 11? "))   
                self.totalValue = self.totalValue + value1   
                    
            else:
                value1 = int(newPlayer.card1.split(' ') [0])
                self.totalValue = self.totalValue + value1 
                        
            if self.totalValue > 21:
                print(newPlayer)
                print(self.totalValue)
                self.totalValue = 0
                print("Total Value is Greater Than 21")
                return "You Lose"
       
            else:
                print(newPlayer)
                print(self.totalValue)  
                              
            
        
    
      
                           
class Main(object):
    def __init__(self):
        self.pot = 150
    def run (self):
        print ("Your pot is $" + str(self.pot))
        bet = int(input("How much you would like to bet? $"))
        turn = Turn()
        dealer = Dealer()
        myCards = turn.playerDecision()
        print(myCards)
        if myCards == "You Lose":
            self.pot = self.pot - int(bet)
            print("=" *30)
        else:
            dealerCards = dealer.dealerDecision(myCards)
            print(dealerCards)
            if dealerCards == "You Win":
                self.pot = self.pot + bet
                print ("Your new pot is " +str(self.pot))
            else: 
                self.pot = self.pot - bet
                if self.pot > 0:
                    print ("Your new pot is " +str(self.pot))
                    print("=" *30)

        while True:                       
            if self.pot == 0:
                print ("You walk away with nothing")
                break
            elif self.pot < 0:
                print ("You owe the casino $" + str(self.pot *-1))
                break            
            decision = input("Do you want to play again? ").lower()
            if decision == 'no':
                print ("You walk away with $" + str(self.pot))
                break
            else:
                Player.usedCards = []
                bet = int(input("How much you would like to bet? $"))
                myCards = turn.playerDecision()
                print(myCards)
                
                if myCards == "You Lose":
                    self.pot = self.pot - bet
                    print ("Your new pot is " + str(self.pot))
                    print("=" *30)
                else:
                    dealerCards = dealer.dealerDecision(myCards)
                    print(dealerCards)
                    if dealerCards == "You Win":
                        self.pot = self.pot + bet
                        print ("Your new pot is " +str(self.pot))
                        print("=" *30)
                    else: 
                        self.pot = self.pot - bet
                        if self.pot > 0 :
                            print ("Your new pot is " +str(self.pot))
        

print ("Welcome to Jack Black's blackjack")  
main = Main()
main.run()

#FUTURE DEV: multiplayer, dealer shows first card, cardcounting probability 