from Game.rules import rule_number_card, Rule
from card_objects import *


def test_same_color_only():
    same_color_args = {"card_1": red_1, "card_2": red_2}
    assert Rule("number_a", rule_number_card, same_color_args).check() is True


def test_same_number_only():
    same_number_args = {"card_1": red_1, "card_2": green_1}
    assert Rule("number_b", rule_number_card, same_number_args).check() is True


def test_same_card():
    same_card_args = {"card_1": red_1, "card_2": red_1}
    assert Rule("number_c", rule_number_card, same_card_args).check() is True


def test_different_number_card():
    different_number_args = {"card_1": red_1, "card_2": green_2}
    assert Rule("number_d", rule_number_card, different_number_args).check() is False


def test_same_color_to_action_card():
    same_color_to_action_cards_args = {"card_1": red_1, "card_2": draw2_red}
    assert Rule("number_e", rule_number_card, same_color_to_action_cards_args).check() is True


def test_different_color_to_action_card():
    different_color_to_action_cards_args = {"card_1": red_1, "card_2": draw2_green}
    assert Rule("number_f", rule_number_card, different_color_to_action_cards_args).check() is False


def test_to_wildcard_normal():
    to_wildcard_normal_args = {"card_1": red_1, "card_2": wild_normal}
    assert Rule("number_g", rule_number_card, to_wildcard_normal_args).check() is True


def test_to_wildcard_draw4():
    to_wildcard_draw4_args = {"card_1": red_1, "card_2": wild_draw4}
    assert Rule("number_h", rule_number_card, to_wildcard_draw4_args).check() is True
