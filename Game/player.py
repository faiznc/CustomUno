from CardObjects.card import Card
from engine import Orchestrator


class Player:
    def __init__(self, cards: list, orchestrator: Orchestrator, name: str = "Player"):
        self.card_pool: list = cards
        self.name = name
        self.Orchestrator_instance: Orchestrator = orchestrator

    def remove_card(self, card: Card):
        self.card_pool.remove(card)

    def add_card(self, card: Card):
        self.card_pool.append(card)

    def get_card_pool(self):
        return self.card_pool

    def get_name(self):
        return self.name

    def propose_card(self, card: Card) -> bool:
        assert card in self.card_pool
        # Propose to orchestrator
        # If orchestrator accepts, return True
        # If orchestrator rejects, return False
        return True

