from CardObjects.card import Card, NumberCard, ActionCard, WildCard
import logging

logging.basicConfig(level=logging.INFO)
rules_log = logging.getLogger("rules-logger")


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
