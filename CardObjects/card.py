import logging

from CardObjects.jsonReader import get_full_card_list
from CardObjects.statics import Action, Color, Wild

card_log = logging.getLogger("card-logger")


class Card:
    def __init__(self, priority: int, desc: str = None):
        # Higher priority = Better
        self.priority = priority
        self.desc = desc

    def __str__(self):
        return self.desc

    def __repr__(self):
        return self.desc


class NumberCard(Card):
    """NumberCard is a card that has a number and a color."""
    def __init__(self, number: int, color: str, priority: int = 1, desc: str = None):
        super().__init__(priority, desc)
        self.number = number
        self.color = color
        self.desc = str(number) + "-" + color


class ActionCard(Card):
    """ActionCard is a card that has an action and a color."""
    def __init__(self, action: str, color: str, priority: int = 5, desc: str = None):
        super().__init__(priority, desc)
        self.action = action
        self.color = color
        self.desc = action + "-" + color


class WildCard(Card):
    """WildCard is a card that ignore colors."""
    def __init__(self, name: str, priority: int = 10, desc: str = None):
        super().__init__(priority, desc)
        self.name = name
        self.desc = name


class ColorCard(Card):
    """ColorCard is a 'virtual' card to save WildCard color selection."""
    def __init__(self, color: str, priority: int = 1, desc: str = None):
        super().__init__(priority, desc)
        self.color = color
        self.desc = color


class CardInitializer:
    def __init__(self):
        self.cards = []
        self.log = logging.getLogger("card-logger")

    def add_card(self, card: Card):
        self.log.info("A card added: " + str(card))
        self.cards.append(card)

    def add_cards(self, cards: list):
        self.log.info("Cards added.")
        self.cards.extend(cards)

    def get_cards(self):
        return self.cards

    def clear_cards(self):
        self.log.info("Cards cleared.")
        self.cards.clear()

    def __str__(self):
        return str(self.cards)

    def get_initialized_cards(self):
        self.log.info("Cards initialized.")
        self.cards = self.initiate_cards_from_json()
        return self.get_cards()

    def initiate_cards_from_json(self, raw_cards: list = get_full_card_list()) -> list:
        self.clear_cards()
        for raw in raw_cards:
            card: Card = construct_card(raw)
            self.add_card(card)
        return self.get_cards()


def get_color_from_card(raw: str) -> Color:
    if Color.RED.value in raw:
        color: Color = Color.RED
    elif Color.BLUE.value in raw:
        color: Color = Color.BLUE
    elif Color.GREEN.value in raw:
        color: Color = Color.GREEN
    elif Color.YELLOW.value in raw:
        color: Color = Color.YELLOW
    else:
        color: Color = None
    return color


def get_action_from_card(raw: str) -> Action:
    action: Action = None
    action = Action.DRAW_TWO if Action.DRAW_TWO.value in raw else action
    action = Action.REVERSE if Action.REVERSE.value in raw else action
    action = Action.SKIP if Action.SKIP.value in raw else action
    return action


def get_wild_from_card(raw: str) -> Wild:
    if Wild.WILD.value in raw:
        wild: Wild = Wild.WILD
    elif Wild.WILD_DRAW_FOUR.value in raw:
        wild: Wild = Wild.WILD_DRAW_FOUR
    else:
        wild = None
    return wild


def construct_card(raw: str) -> any:
    wild_data = get_wild_from_card(raw)
    if wild_data:
        card_log.info("-Wild card-")
        if wild_data is Wild.WILD:
            priority: int = 5  # For normal wild
        else:
            priority: int = 10  # For draw 4
        card = WildCard(wild_data.value, priority)

    else:
        # log.info("-Colored card-")
        action_data: Action = get_action_from_card(raw)
        color_data: Color = get_color_from_card(raw)
        if action_data:
            card_log.info("-Action card-")
            card = ActionCard(action_data.value, color_data.value)
        else:
            card_log.info("-Number card-")
            number = int(raw.split(color_data.value)[1])
            card = NumberCard(number, color_data.value)
    card_log.info("Final Card: " + str(card))
    return card
