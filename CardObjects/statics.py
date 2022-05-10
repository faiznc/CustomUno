from enum import Enum


class Color(Enum):
    """Colors of cards"""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"


class Action(Enum):
    """Actions of cards"""
    DRAW_TWO = "Draw2"
    REVERSE = "Reverse"
    SKIP = "Skip"


class Wild(Enum):
    """Wild cards"""
    WILD = "Wild"
    WILD_DRAW_FOUR = "Draw4"


# Class might be unused.
class Number(Enum):
    """Numbers of cards"""
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
