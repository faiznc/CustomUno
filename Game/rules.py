from CardObjects.card import Card, NumberCard, ActionCard, WildCard
from engine import Rule
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


red_1 = NumberCard(1, "red")
red_2 = NumberCard(2, "red")
red_3 = NumberCard(3, "red")
green_1 = NumberCard(1, "green")
green_2 = NumberCard(2, "green")

draw2_red = ActionCard("Draw2", "red")
draw2_green = ActionCard("Draw2", "green")
skip_red = ActionCard("Skip", "red")
reverse_yellow = ActionCard("Reverse", "yellow")

wild_draw4 = WildCard("Draw4", 10)
wild_normal = WildCard("Wild", 5)


# Assertion - To be unit test...
same_number_args = {"card_1": red_1, "card_2": red_2}
same_color_number_card_args = {"card_1": red_1, "card_2": green_1}
same_card_args = {"card_1": red_1, "card_2": red_1}
different_number_args = {"card_1": red_1, "card_2": green_2}

same_color_to_action_cards_args = {"card_1": red_1, "card_2": draw2_red}
different_color_to_action_cards_args = {"card_1": red_1, "card_2": draw2_green}

to_wildcard_normal_args = {"card_1": red_1, "card_2": wild_normal}
to_wildcard_draw4_args = {"card_1": red_1, "card_2": wild_draw4}

a = Rule("a", rule_number_card, same_number_args).check()
print("a = ", a)
assert a is True

b = Rule("b", rule_number_card, same_color_number_card_args).check()
print("b = ", b)
assert b is True

c = Rule("c", rule_number_card, same_card_args).check()
print("c = ", c)
assert c is True

d = Rule("e", rule_number_card, different_number_args).check()
print("d = ", d)
assert d is False
