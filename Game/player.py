import logging

from CardObjects.card import Card
from CardObjects.deck import Deck
from Game.engine import Orchestrator


class Player:
    def __init__(self, orchestrator: Orchestrator, name: str = "Player"):
        self.Orchestrator_instance: Orchestrator = orchestrator
        self.card_pool: Deck = Deck(is_empty=True)
        self.name = name
        self.log = logging.getLogger("player-logger")

    def remove_card(self, card: Card):
        self.card_pool.remove(card)

    def add_card(self, card: Card):
        self.card_pool.add_card(card)

    def add_cards(self, cards: list):
        self.card_pool.add_cards(cards)

    def get_current_cards(self):
        return self.card_pool.cards

    def get_card_pool(self):
        return self.card_pool

    def get_name(self):
        return self.name

    def propose_card(self, card: Card) -> bool:
        assert card in self.card_pool
        # Propose to orchestrator
        # If orchestrator accepts, return True
        # If orchestrator rejects, return False
        # Then handle the card removal from card pool (if accepted)
        return True

    def ask_new_card(self):
        """Ask the controller for a new card"""
        pass

    def declare_uno(self):
        pass


