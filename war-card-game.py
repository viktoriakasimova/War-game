from random import shuffle

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck:
    
    def __init__(self):
        suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
        values = ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks] 
                
    def shuffle(self):
        shuffle(self.cards)
        
    def deal_one(self):
        return self.cards.pop()        

class Player:
    
    def __init__(self,name):
        self.name = name
        self.cards_in_hand = [] 
        
    def remove_one(self):
        # [0] - top of the deck, [-1] - bottom of the deck
        return self.cards_in_hand.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == list:
            self.cards_in_hand.extend(new_cards)
        else:
            self.cards_in_hand.append(new_cards)
    
    def __repr__(self):
        return "Player {} has {} cards in hand.".format(self.name, len(self.cards_in_hand))

# GAME SETUP

# Players setup
player_one = Player("One")
player_two = Player("Two")

# A new deck setup
deck = Deck()
deck.shuffle()

# Divide the cards in the deck equally between two players 
for x in range(26):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())
    
game_on = True

# GAME LOGIC

num_of_rounds = 0
while game_on:
    
    num_of_rounds += 1
    print("Round {}".format(num_of_rounds))
    
    # Check if one of the players has run out of cards, in which case the game is over:
    if len(player_one.cards_in_hand) == 0:
        print("Player One has run out of cards! Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.cards_in_hand) == 0:
        print("Player Two has run out of cards! Player One Wins!")
        game_on = False
        break
    
    # Start a new round of the game and reset the cards in play
    player_one_cards_in_play = []
    player_one_cards_in_play.append(player_one.remove_one())
    
    player_two_cards_in_play = []
    player_two_cards_in_play.append(player_two.remove_one())
    
    # Get players to compare their cards in play to see who wins
    comparing_cards = True

    while comparing_cards:
        # Player One's card is higher
        if player_one_cards_in_play[-1].value > player_two_cards_in_play[-1].value:

            # Player One wins and gets both cards
            player_one.add_cards(player_one_cards_in_play)
            player_one.add_cards(player_two_cards_in_play)
                
            # The round has finished
            comparing_cards = False
        
        # Player Two's card is higher
        elif player_one_cards_in_play[-1].value < player_two_cards_in_play[-1].value:

            # Player Two wins and gets both cards
            player_two.add_cards(player_one_cards_in_play)
            player_two.add_cards(player_two_cards_in_play)
            
            # The round has finished
            comparing_cards = False

        # The cards of both players are equal
        else:
            print("WAR HAS STARTED!")
            
            # Each player grabs 3 new cards and continues comparing.
            # But at first we check if each player has enough cards (3 or more) to continue the war.

            # Check if Player One has run out of cards:
            if len(player_one.cards_in_hand) < 3:
                print("Player One is unable to continue the war!")
                print("Player Two wins the game!")
                game_on = False
                break
            # Check if Player Two has run out of cards:
            elif len(player_two.cards_in_hand) < 3:
                print("Player Two is unable to continue the war!")
                print("Player One wins the game!")
                game_on = False
                break
                
            # If players have enough cards, the war continues, and each player add 3 new cards to their cards in play.
            else:
                for num in range(3):
                    player_one_cards_in_play.append(player_one.remove_one())
                    player_two_cards_in_play.append(player_two.remove_one())
