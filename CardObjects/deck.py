import random

from CardObjects.card import CardInitializer


class Deck:
    """Main class for a stack of cards.
    Can be used to group all used cards that already played to be inserted again to the main pool."""
    def __init__(self, cards: list = CardInitializer().get_initialized_cards()):
        self.cards = cards
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck."""
        return self.cards.pop()

    def draw_n(self, n: int):
        """Draw n cards from the deck."""
        return [self.cards.pop() for _ in range(n)]

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __delitem__(self, index):
        del self.cards[index]

    def __contains__(self, item):
        return item in self.cards
