import logging
from CardObjects import deck
from CardObjects.card import Card
from CardObjects.deck import Deck
from Game.rules import Rule

logging.basicConfig(level=logging.INFO)
eng_log = logging.getLogger("engine-logger")


class Player:
    def __init__(self, orchestrator, name: str = "Player"):
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
        return self.card_pool.get_cards()

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


# My intention are Orchestrator only produce a response
# whether a card(s) (or a combos) is allowed to be used or not.
# The user must choose their own way to decide what card to be used
# to give them freedom of how they play their cards.
# Including choosing whether they want to skip a turn even though they have the matching cards.


class Orchestrator:

    def __init__(self, rules: list[Rule]):
        self.rules = rules
        self.main_cards = deck.Deck(cards=[])
        self.played_cards = deck.Deck(cards=[])
        self.current_card: Card = None
        self.player_data: PlayerDataSync = PlayerDataSync()
        self.card_distribution_count = 8
        # Player turn rotation data
        self.first_turn_player_index = 0
        self.is_rotation_incremented = False
        self.log = logging.getLogger("orchestrator-logger")

    def set_current_card(self, card: Card):
        self.current_card = card

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def add_rules(self, rules: list[Rule]):
        self.rules.extend(rules)

    def set_players(self, players: list[Player]):
        for x in range(len(players)):
            self.player_data.set_player_data_by_index(x, players[x])

    def get_players(self) -> list[Player]:
        return self.player_data.get_players()

    def initialize_cards(self):
        self.log.info("Initializing orchestrator.")
        self.main_cards.add_cards(deck.Deck().cards)
        self.main_cards.shuffle()
        self.log.info("Number of card in reserved deck: {}".format(len(self.main_cards)))
        self.log.info("Number of card in played deck: {}".format(len(self.played_cards)))
        # Distribute cards to players
        for player in self.player_data.get_players():
            player.add_cards(self.draw_cards(self.card_distribution_count))

        # Set current main card
        self.set_current_card(self.draw_card())
        self.log.info("Current card: {}".format(self.current_card))
        self.log.info("Number of card in reserved deck: {}".format(len(self.main_cards)))

    # Must be executed after card cycle.
    def add_played_card_to_main_cards(self):
        if len(self.main_cards) < 20:
            played = deck.Deck(self.played_cards).shuffle()
            # TODO Need to check validity of the shuffling
            temp_main_cards = self.main_cards
            # To make sure that card that present in main_cards will be played
            self.main_cards = played + temp_main_cards

    def dispose_used_card(self, card: Card):
        self.played_cards.add_card(card)

    def check_card_proposal(self, proposed_card: Card) -> bool:
        rule_args = {"card_1": self.current_card, "card_2": proposed_card}
        for rule in self.rules:
            rule.set_kwargs(rule_args)
            self.log.debug(f"Checking rule {rule.name}")
            if rule.check() is False:
                self.log.info("Rule {} is not satisfied.".format(rule.name))
                return False
            else:
                self.log.debug("Rule {} is satisfied.".format(rule.name))
                pass
        return True

    def handle_card_proposal(self, proposed_card: Card):
        if self.check_card_proposal(proposed_card):
            self.log.debug("Card {} is allowed to be used.".format(proposed_card))
            self.dispose_used_card(proposed_card)
            self.set_current_card(proposed_card)
            self.log.info("Number of card in reserved deck: {}".format(len(self.main_cards)))
            self.log.info("Number of card in played deck: {}".format(len(self.played_cards)))
            return True
        else:
            return False

    def draw_card(self) -> Card:
        return self.main_cards.draw()

    def draw_cards(self, n: int) -> list[Card]:
        return self.main_cards.draw_n(n)

    def handle_card_cycle(self):
        self.log.info("Handling card cycle.")
        self.add_played_card_to_main_cards()
        self.log.info("Number of card in reserved deck: {}".format(len(self.main_cards)))
        self.log.info("Number of card in played deck: {}".format(len(self.played_cards)))

    def propose_combos(self, combos: list[Card]) -> bool:
        pass


class PlayerDataSync:
    def __init__(self):
        self.player_data = {}
        self.log = logging.getLogger("player-data-sync-logger")

    def set_player_data_by_index_complete(self, player_index: int, player_name: str, card_count: int, instance: Player):
        self.player_data[player_index] = {
            'name': player_name,
            'card_count': card_count,
            'instance': instance
        }

    def set_player_data_by_index(self, player_index: int, instance: Player):
        self.player_data[player_index] = {
            'name': instance.name,
            'card_count': len(instance.card_pool),
            'instance': instance
        }

    def get_player_data_by_index(self, player_index: int):
        return self.player_data[player_index]

    def get_all_data(self):
        return self.player_data

    def get_players(self) -> list[Player]:
        players = []
        for player_data in self.player_data.values():
            players.append(player_data['instance'])
        return players
