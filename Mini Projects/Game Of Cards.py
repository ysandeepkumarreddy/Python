import random  # Import random module

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Create a list of suits
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Create a list of ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  # Create dictionary of values for each rank


# Create a class for the cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # create a suit attribute
        self.rank = rank  # create a rank attribute
        self.value = values[rank]  # create a value attribute for the cards

# create a str method for the cards
    def __str__(self):
        # return the rank of the card and the suit
        return self.rank + ' of ' + self.suit

# Create a class for the deck of cards


class Deck:
    def __init__(self):  # create a deck attribute
        self.all_cards = []  # create an empty list for the deck
        for suit in suits:  # loop through the suits
            for rank in ranks:
                create_card = Card(suit, rank)  # create a card class
                # append the card to the deck
                self.all_cards.append(create_card)

    def shuffle(self):  # create a shuffle method
        random.shuffle(self.all_cards)  # shuffle the deck

    def deal_one(self):
        # deal a card by popping the last card in the deck
        return self.all_cards.pop()


# Create a class for the Player of cards
class Player:
    def __init__(self, name):
        self.name = name  # create a name attribute
        self.all_cards = []  # create an empty list for the player

    def remove_one(self):
        # remove a card from the player's hand
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):  # add a card to the player's hand
        if type(new_cards) == type([]):  # check if the new_cards is a list
            # add the new_cards to the player's hand
            self.all_cards.extend(new_cards)
        else:
            # add the new_cards to the player's hand
            self.all_cards.append(new_cards)

    def __str__(self):  # create a str method for the player
        # return the number of cards in the player's hand
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player('Player One')
player_two = Player('Player Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):  # loop through the deck 26 times
    player_one.add_cards(new_deck.deal_one())  # deal a card to the player
    player_two.add_cards(new_deck.deal_one())  # deal a card to the player

game_on = True  # create a game_on variable
round_number = 0  # create a round_number variable
while game_on:  # loop through the game

    round_number += 1  # increase the round number by one
    print(f'Round {round_number}')  # print the round number

    if len(player_one.all_cards) == 0:  # check if the player has any cards
        # print that the player has no cards left
        print('Player One has no cards left')
        print('Player Two Won!!')  # print that player two has won the game
        game_on = False  # set game_on to False
        break  # break the loop
    if len(player_two.all_cards) == 0:  # check if the player has any cards
        # print that the player has no cards left
        print('Player Two has no cards left')
        print('Player One has Won!!')  # print that player one has won the game
        game_on = False  # set game_on to False
        break  # break the loop

    # otherwise, the game continues

    player_one_cards = []  # create a list for player one's cards
    # remove a card from the player's hand
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []  # create a list for player two's cards
    # remove a card from the player's hand
    player_two_cards.append(player_two.remove_one())

    at_war = True  # create a at_war variable
    while at_war:  # loop through the game
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # add the card to the player one's hand
            player_one.add_cards(player_one_cards)
            # add the card to the player two's hand
            player_one.add_cards(player_two_cards)

            at_war = False  # set at_war to False

        # check if the player one's card is greater than the player two's card
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # add the player two's card to the player two's hand
            player_two.add_cards(player_two_cards)
            # Player Two gets Player One's card
            player_one.add_cards(player_two_cards)

            at_war = False  # set at_war to False

        else:
            print('War!!')

            if len(player_one.all_cards) < 3:  # check if the player has less than 3 cards
                # print that the player has no cards left
                print('Player One has no cards left')
                # print that player two has won the game
                print('Player Two Won!!')
                game_on = False  # set game_on to False
                break  # break the loop
            elif len(player_two.all_cards) < 3:
                print('Player Two has no cards left')
                print('Player One has Won!!')
                game_on = False  # set game_on to False
                break  # break the loop
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
