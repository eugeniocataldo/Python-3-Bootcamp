# %% [markdown]
# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# %% [markdown]
# # Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
# 
# Here are the requirements:
# 
# * You need to create a simple text-based [BlackJack](https://en.wikipedia.org/wiki/Blackjack) game
# * The game needs to have one player versus an automated dealer.
# * The player can stand or hit.
# * The player must be able to pick their betting amount.
# * You need to keep track of the player's total money.
# * You need to alert the player of wins, losses, or busts, etc...
# 
# And most importantly:
# 
# * **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**
# 
# 
# Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
# 
# # HAVE FUN!


# %%
import random

### Global variables to assign attributes to cards
SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
VALUES = {
    "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, 
    "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10,
    "Queen" : 10, "King" : 10, "Ace" : 11
    }


# %%

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # Calculate the value based on a LUT defined as a global variable
        try: 
            self.value =  VALUES[rank]
        except KeyError:
            print("The rank needs to be one of these:\n", RANKS)

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.all_cards = []

        # Fill up the deck with all cards
        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):


        # Add a check if the deck is finished, in which case I reshuffle and use it again
        if len(self.all_cards) == 0:
            print("Deck is finished, will reshuffle all the cards in")

            for suit in SUITS:
                for rank in RANKS:
                    self.all_cards.append(Card(suit, rank))

            self.shuffle()

        return self.all_cards.pop()


class Player:

    def __init__(self, name, initial_money):
        self.name = name
        self.money = initial_money
        self.hand = Hand()

    def __str__(self):
        return f"Player {self.name} has {self.money}$"

    def bet(self, amount):
        if amount > self.money:
            raise InterruptedError("You don't have that much money, we don't accept your shitty house as payment")
        else:
            self.money -= amount
            print(f"{amount}$ bet. You still have {self.money}$")

    def win(self, amount):
        self.money += amount

    def draw(self, card: Card):
        self.hand.draw_card(card)

    def discard_hand(self):
        self.hand.reset_hand()


class Hand:

    def __init__(self):
        self.all_cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.all_cards)

    # Draw one card
    def draw_card(self, card: Card):
        self.all_cards.append(card)

    # Discard all cards and start with an empty hand
    def reset_hand(self):
        self.all_cards = []


    # Calculate the value of the hand, given the aces
    def value(self):
        total_value = 0
        aces = 0

        for card in self.all_cards:
            total_value += card.value
            if card.rank == "Ace":
                aces += 1

        # Now account for the aces being 11 or 1
        while total_value > 21 and aces > 0:
            total_value -= 10
            aces -= 1
        
        return total_value


def ask_yes_or_no(question):
    """
    Simple wrapper around the yes/no input() function, to add checks on what the user writes
    """
    
    while True:
        yes_or_no = input(question)
        if yes_or_no != 'Y' and yes_or_no != 'N':
            continue
        else:
            break

    return yes_or_no



# %%

### Game flow

# Create deck and players
my_deck = Deck()
player_1 = Player("One", 100)
dealer = Player("Dealer", "infinite")

# Game starts. Check if player is at 0 and needs to buy more chips, and discard previous hands
keep_playing = 'Y'
while keep_playing == 'Y':
    player_1.discard_hand()
    dealer.discard_hand()
    print(player_1)
    my_deck.shuffle()



    if player_1.money <= 0:
        print("Bro, you're broke")
        charging_more = ask_yes_or_no("Write 'Y' if you want to charge more money and 'N' if you don't")

        if charging_more == 'Y':
            player_1.win(int(input("How much?")))
        else:
            print("Then get out of here!")
            keep_playing = 'N'
            break

    # Player 1 places a bet
    valid_bet = False
    while not valid_bet:
        try:
            bet = int(input("Player 1, how much do you want to bet?"))
            player_1.bet(amount=bet)
        except ValueError:
            print("Make sure to type in a digit")
        except InterruptedError: # This error is raised manually in the Player class
            print(f"You only have {player_1.money}$, we don't accept your shitty house as payment. Please bet an amount you own")
        else:
            valid_bet = True


    # Hand card to dealer and player
    dealer.draw(my_deck.deal_one())
    print(f"The dealer has: {str(dealer.hand)} in the hand")
    print("The dealer gets another card face down")
    dealer.draw(my_deck.deal_one())

    player_1.draw(my_deck.deal_one())
    player_1.draw(my_deck.deal_one())
    print(player_1)
    print(f"Player 1 has {str(player_1.hand)} in the hand")

    # Player plays:
    busted = False
    hit_or_stay = ask_yes_or_no("Write 'Y' if you want to hit and 'N' if you want to stay")

    while hit_or_stay == 'Y' and not busted:
        player_1.draw(my_deck.deal_one())
        print(player_1)
        print(f"Player 1 has {str(player_1.hand)} in the hand")

        if player_1.hand.value() > 21:
            busted = True
            print("BUSTEEEEEEEED!")
        else:
            hit_or_stay = ask_yes_or_no("Write 'Y' if you want to hit and 'N' if you want to stay")


    # Dealer plays:
    if not busted:
        print(f"The dealer has: {str(dealer.hand)} in the hand")
        while dealer.hand.value() <= player_1.hand.value() and dealer.hand.value() < 21:
            dealer.draw(my_deck.deal_one())
            print(f"The dealer has: {str(dealer.hand)} in the hand")


    # Win check and give money
    if busted or player_1.hand.value() < dealer.hand.value() <= 21:
        print(f"The dealer won your incredible bet of {bet}$")
    elif player_1.hand.value() == dealer.hand.value():
        print("That's a tie, you both had 21") # Only case in which this can happen is if both are 21, for the while loop above
    else:
        print("Dealer busted") # For how the game is constructed, the dealer keeps drawing unless it's 21 or busted, so the player only wins if the dealer busts
        player_1.win(amount=2*bet) 
        print(f"You won the incredible amount of {bet}$!! You can now open your own casino")

    # Play again check
    print(player_1)
    print("Another hand?")
    keep_playing = ask_yes_or_no("Write 'Y' if you want to keep playing and 'N' if you want to stop")


# %%
