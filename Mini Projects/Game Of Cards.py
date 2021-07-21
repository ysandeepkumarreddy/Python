import random  # Import random module

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Create a list of suits
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')  # Create a list of ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  # Create dictionary of values for each rank


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
        return self.all_cards.pop()  # Deal the top card


new_deck = Deck()  # Create a deck
new_deck.shuffle()  # Shuffle the deck
mycard = new_deck.dealone()  # Deal the top card
print(mycard)  # Print the card
print(len(new_deck.all_cards))  # Print the number of cards left in the deck
