from CardObjects.card import Card, NumberCard, ActionCard, WildCard
import logging

logging.basicConfig(level=logging.INFO)
rules_log = logging.getLogger("rules-logger")


class Rule:
    def __init__(self, name: str = None,
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

def rule_number_card(card_1: Card, card_2: Card) -> bool:
    result: bool = None
    if type(card_1) is NumberCard:
        if type(card_2) is NumberCard:
            if card_1.color == card_2.color or card_1.number == card_2.number:
                rules_log.info("Number to Number with the same color / number")
                result = True
            else:
                rules_log.info("Number to Number with different color / number")
                result = False

        elif type(card_2) is ActionCard:
            rules_log.info("Number to Action.")
            if card_1.color == card_2.color:
                result = True
            else:
                result = False

        elif type(card_2) is WildCard:
            rules_log.info("Number to Wild.")
            result = True

    return result


def rule_action_card(card_1: Card, card_2: Card) -> bool:
    result: bool = None
    if type(card_1) is ActionCard:
        if type(card_2) is NumberCard:
            rules_log.info("Action to Number.")
            if card_1.color == card_2.color:
                result = True
            else:
                result = False

        elif type(card_2) is ActionCard:
            rules_log.info("Action to Action.")
            if card_1.color == card_2.color:
                result = True
            elif card_1.action == card_2.action:
                result = True
            else:
                result = False

        elif type(card_2) is WildCard:
            rules_log.info("Action to Wild.")
            result = True

    return result


def rule_wild_card(card_1: Card, card_2: Card) -> bool:
    result: bool = None
    if type(card_1) is WildCard:
        if type(card_2) is NumberCard:
            rules_log.info("Wild to Number.")
            result = True
        elif type(card_2) is ActionCard:
            rules_log.info("Wild to Action.")
            result = True
        elif type(card_2) is WildCard:
            rules_log.info("Wild to Wild.")
            result = True

    return result


def rule_color_states(card_1: Card, card_2: Card) -> bool:
    result: bool = None
    if type(card_2) is WildCard:  # Ignore if next card is a Wild card
        result = True
    elif card_1.color == card_2.color:  # Assert same color on Number and Action cards
        result = True
    else:
        result = False
    return result
