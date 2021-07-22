import random  # Import random module

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Create a list of suits
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Create a list of ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  # Create dictionary of values for each rank


class Card:  # Card class
    def __init__(self, suit, rank):  # Card constructor
        self.suit = suit  # suit is a string
        self.rank = rank  # rank is an integer
        self.value = values[rank]  # value is an integer

    def __str__(self):  # string representation of a Card
        return self.rank + ' of ' + self.suit  # returns a string


class Deck:  # Deck class
    def __init__(self):  # Deck constructor
        self.all_cards = []  # Create empty list for cards
        for suit in suits:  # For each suits
            for rank in ranks:
                create_card = Card(suit, rank)  # Creates a card
                # Add card to list of all cards
                self.all_cards.append(create_card)

    def shuffle(self):  # Shuffle the deck
        random.shuffle(self.all_cards)  # Shuffle the list of cards

    def dealone(self):
        return self.all_cards.pop()  # Deal the top card from the deck


class Player:
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []  # list of cards in player's hand

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)  # return the last card in the list

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player("One")  # Create a player1
player_two = Player("Two")  # Create a player2

new_deck = Deck()  # Create a deck
new_deck.shuffle()  # Shuffle the deck


for x in range(26):  # Deal 26 cards to each player
    player_one.add_cards(new_deck.dealone())  # Deal card to player1
    player_two.add_cards(new_deck.dealone())  # Deal card to player2

game_on = True  # Game is on

round_num = 0  # Round number
while game_on:  # While game is on

    round_num += 1  # Increment round number
    print(f"Round {round_num}")  # Print round number

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")  # Player 1 is out of cards
        print("Player Two Wins!")   # Player 2 wins
        game_on = False  # Game is over
        break   # Exit the loop

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")  # Player 2 is out of cards
        print("Player One Wins!")   # Player 1 wins
        game_on = False  # Game is over
        break   # Exit the loop

    # Otherwise, the game is still on!

    # Start a new round and reset current cards "on the table"
    player_one_cards = []   # List of cards in player 1's hand
    # Add top card from player 1's hand to table
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []   # List of cards in player 2's hand
    # Add top card from player 2's hand to table
    player_two_cards.append(player_two.remove_one())

    at_war = True   # Set at_war to True

    while at_war:   # While at war, keep dealing cards

        # If player 1's card is higher than player 2's card
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            # Add player 1's cards to player 1's hand
            player_one.add_cards(player_one_cards)
            # Add player 2's cards to player 1's hand
            player_one.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False  # Set at_war to False

        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 3:
                # Player 1 is out of cards
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")  # Player 2 wins
                game_on = False  # Game is over
                break   # Exit the loop

            elif len(player_two.all_cards) < 3:  # Check to see if a player is out of cards
                # Player 2 is out of cards
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")  # Player 1 wins
                game_on = False  # Game is over
                break       # Exit the loop
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(3):  # Loop thrice
                    # Add player 1's cards to table
                    player_one_cards.append(player_one.remove_one())
                    # Add player 2's cards to table
                    player_two_cards.append(player_two.remove_one())
