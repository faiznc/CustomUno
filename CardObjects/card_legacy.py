class Card:
    def __init__(self, priority: int, desc: str = None):
        self.priority = priority  # Higher = Better
        self.desc = desc

    def __str__(self):
        return self.desc

    def __repr__(self):
        return self.desc


class NumberCard(Card):
    def __init__(self, number: int, color: str, priority: int = 1, desc: str = None):
        super().__init__(priority, desc)
        self.number = number
        self.color = color
        self.desc = str(number) + "-" + color


class PlusCard(Card):
    def __init__(self, count: int, color: str, priority: int, desc: str = None):
        super().__init__(priority, desc)
        self.count = count
        self.color = color
        self.desc = "+" + str(count) + "-" + color


class ActionCard(Card):
    def __init__(self, action: str, color: str, priority: int, desc: str = None):
        super().__init__(priority, desc)
        self.action = action
        self.color = color
        self.desc = action + " " + color


def generate_single_type_cards(class_name: any, qty: int, **kwargs) -> list:
    cards: list = []
    for x in range(qty):
        item = class_name(**kwargs)
        cards.append(item)
    return cards


def generate_multi_colored_cards(class_name, qty: int, **kwargs) -> list:
    """Generate each color of card from every color on specific class by an amount"""
    cards: list = []
    for x in range(qty):
        red_card = class_name(**kwargs, color="RED")
        blue_card = class_name(**kwargs, color="BLUE")
        green_card = class_name(**kwargs, color="GREEN")
        yellow_card = class_name(**kwargs, color="YELLOW")
        cards.append(red_card)
        cards.append(blue_card)
        cards.append(green_card)
        cards.append(yellow_card)
    return cards


def generate_number_zero() -> list:
    return generate_multi_colored_cards(NumberCard, qty=1, number=0)


def generate_number_cards() -> list:
    local_pool: list = generate_number_zero()
    for x in range(9):
        x = x + 1
        local_pool += generate_multi_colored_cards(NumberCard, 2, number=x)
    return local_pool


card_pool: list = []

card_pool += generate_number_cards()


print(len(card_pool))
print(card_pool)
