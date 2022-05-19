import logging
import random

from CardObjects import deck
from CardObjects.card import Card
from CardObjects.deck import Deck
from Game.rules import Rule

logging.basicConfig(level=logging.INFO)
eng_log = logging.getLogger("engine-logger")


class Player:
    def __init__(self, orchestrator, name: str = "Player"):
        self.orchestrator: Orchestrator = orchestrator
        self.card_pool: Deck = Deck(is_empty=True)
        self.name = name
        self.is_playing_flag = False
        self.log = logging.getLogger("player-logger")

    def set_playing_flag(self, flag: bool):
        self.is_playing_flag = flag

    def remove_card(self, card: Card):
        self.card_pool.remove_card(card)

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
        new_card = self.orchestrator.draw_card()
        self.add_card(new_card)

    def declare_uno(self):
        pass

    def play(self):
        """Play the cards in the card pool"""
        if not self.is_playing_flag:
            return

        # Using simple input for now
        print("Player " + self.name + ":")
        temp_played_card: Card = self.orchestrator.get_current_card()
        print("Current card: \n"
              " ----  " + str(temp_played_card) + "  ----")
        print("Your cards: " + str(self.get_current_cards()))
        print("Your turn:")
        print("1. Play a card")
        print("2. Ask for a new card")
        print("3. Declare UNO")
        print("4. Pass")
        print("5. Quit")
        choice = input("Your choice: ")
        if choice == "1":
            # Play a card from the card pool
            # Proposing which card to be played
            print("Which card do you want to play?")
            for index in range(self.card_pool.get_size()):
                print(str(index + 1) + ". " + str(self.card_pool[index]))
            choice: int = input("Your choice: ")
            if choice.isdigit():
                choice = int(choice) - 1
                if choice > 0 and choice <= self.card_pool.get_size():
                    card = self.card_pool.get_card_by_index(choice)
                    if self.propose_card(card):
                        self.log.info("Current card: " + str(temp_played_card))
                        self.log.info("Card " + str(card) + " accepted")
                        self.remove_card(card)
                        # self.Orchestrator_instance.add_card(card)
                        # self.Orchestrator_instance.next_player()
                    else:
                        self.log.info("Current card: " + str(temp_played_card))
                        self.log.info("Card " + str(card) + " rejected")
                        print("Card rejected")
                else:
                    print("Invalid choice")

        elif choice == "2":
            self.ask_new_card()
        elif choice == "3":
            self.declare_uno()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            print("Invalid choice")
            self.play()


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
        self.is_playing = None
        self.is_first_turn = True

    def set_current_card(self, card: Card):
        self.current_card = card

    def get_current_card(self):
        return self.current_card

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def add_rules(self, rules: list[Rule]):
        self.rules.extend(rules)

    def set_players(self, players: list[Player]):
        for x in range(len(players)):
            self.player_data.set_player_data_by_index(x, players[x])

    def get_players(self) -> list[Player]:
        return self.player_data.get_players()

    def get_player_instance_by_index(self, player_index: int) -> Player:
        return self.player_data.get_player_data_by_index(player_index)['instance']

    def get_player_name_by_index(self, player_index: int) -> str:
        return self.player_data.get_player_data_by_index(player_index)['name']

    def set_player_to_play(self, player_index: int):
        self.first_turn_player_index = player_index
        self.get_player_instance_by_index(player_index).set_playing_flag(True)
        self.log.info("Player " + self.get_player_name_by_index(player_index) + " is now playing")

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

    def start_game(self):
        self.initialize_cards()
        self.is_playing = True
        self.log.info("Orchestrator started.")

        # Choose first player
        self.first_turn_player_index = random.randint(0, len(self.player_data.get_players()) - 1)
        self.log.info("First player are: {}".format(self.get_player_name_by_index(self.first_turn_player_index)))

        while self.is_playing:
            self.log.info("Current player: {}".format(self.get_player_name_by_index(self.first_turn_player_index)))
            self.set_player_to_play(self.first_turn_player_index)
            self.get_player_instance_by_index(self.first_turn_player_index).play()
            self.first_turn_player_index = self.get_next_player_index()
            self.is_first_turn = False