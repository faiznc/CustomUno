import logging
import random

from CardObjects.card import CardInitializer, Card

# NOTE: Maybe it's better to move this module to Game folder

class Deck:
    """Main class for a stack of cards.
    Can be used to group all used cards that already played to be inserted again to the main pool."""

    def __init__(self, cards: list = CardInitializer().get_initialized_cards(), is_empty: bool = False) -> object:
        self.cards = cards
        if is_empty:
            self.cards = []
        self.shuffle()
        self.log = logging.getLogger("deck-logger")

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def clear(self):
        self.cards.clear()

    def add_card(self, card: Card):
        self.cards.append(card)

    def add_cards(self, cards: list):
        self.cards.extend(cards)

    def draw(self):
        """Draw a card from the deck."""
        card = self.cards.pop()
        self.log.info("Card count= " + str(len(self.cards)))
        return card

    def draw_n(self, n: int):
        """Draw n cards from the deck."""
        cards = []
        for i in range(n):
            cards.append(self.cards.pop())
        self.log.info("Card count= " + str(len(self.cards)))
        return cards

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
