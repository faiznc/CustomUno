import logging
from CardObjects import deck
from CardObjects.card import Card

logging.basicConfig(level=logging.INFO)
eng_log = logging.getLogger("engine-logger")

class Rule:
    def __init__(self, name: str,
                 function: callable = None,
                 kwargs: dict = None,
                 priority: int = 0,
                 desc: str = "A rule."):

        self.name = name
        self.priority = priority
        self.desc = desc
        self.functions: callable = function
        self.kwargs: dict = kwargs
        self.allowed_card_types: list[Card] = []

    def get_priority(self) -> int:
        return self.priority

    def set_priority(self, priority: int):
        self.priority = priority

    def set_function(self, function: callable):
        self.functions = function

    def set_kwargs(self, kwargs: dict):
        self.kwargs = kwargs

    def check(self) -> bool:
        """Check if the rule is satisfied. \n
        Return *True* if the rule is used; \n
        Return *False* if the rule is not satisfied; \n
        Return *None* if the rule is not used."""
        return self.functions(**self.kwargs)

    def allowed_card_types(self) -> list[Card]:
        return self.allowed_card_types


# TODO Combo class. Can also use Rule object to make sure the behavior is correct.

# My intention are Orchestrator only produce a response
# whether a card(s) (or a combos) is allowed to be used or not.
# The user must choose their own way to decide what card to be used
# to give them freedom of how they play their cards.
# Including choosing whether they want to skip a turn even though they have the matching cards.
class Orchestrator:
    def __init__(self, rules: list[Rule]):
        self.rules = rules
        self.main_cards: list[Card] = []
        self.played_cards: list[Card] = []
        # self.log = logging.getLogger("orchestrator-logger")

    def add_played_card_to_main_cards(self):
        if len(self.main_cards) < 20:
            played = deck.Deck(self.played_cards).shuffle()
            # TODO Need to check validity of the shuffling
            temp_main_cards = self.main_cards
            # To make sure that card that present in main_cards will be played
            self.main_cards = played + temp_main_cards


    def propose_cards(self, card: Card) -> bool:
        pass

    def propose_combos(self, combos: list[Card]) -> bool:
        pass




# def rule_a(n: int) -> bool:
#     return n == 1
#
#
# rule_1 = Rule("rule_1", 1, "rule number 1")
# rule_1.set_function(rule_a)
# rule_1.set_kwargs({"n": 1})
#
# a = rule_1.check()
# print(a)



