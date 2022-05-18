from Game.rules import rule_wild_card, Rule
from card_objects import *


def test_wild_normal_to_wild_normal():
    wild_normal_to_wild_normal_args = {"card_1": wild_normal, "card_2": wild_normal}
    assert Rule("number_a", rule_wild_card, wild_normal_to_wild_normal_args).check() is True


def test_wild_normal_to_wild_draw4():
    wild_normal_to_wild_draw4_args = {"card_1": wild_normal, "card_2": wild_draw4}
    assert Rule("number_b", rule_wild_card, wild_normal_to_wild_draw4_args).check() is True


def test_wild_draw4_to_wild_normal():
    wild_draw4_to_wild_normal_args = {"card_1": wild_draw4, "card_2": wild_normal}
    assert Rule("number_c", rule_wild_card, wild_draw4_to_wild_normal_args).check() is True


def test_wild_draw4_to_wild_draw4():
    wild_draw4_to_wild_draw4_args = {"card_1": wild_draw4, "card_2": wild_draw4}
    assert Rule("number_d", rule_wild_card, wild_draw4_to_wild_draw4_args).check() is True


def test_wild_draw4_to_number_card():
    wild_draw4_to_number_card_args = {"card_1": wild_draw4, "card_2": red_1}
    assert Rule("number_e", rule_wild_card, wild_draw4_to_number_card_args).check() is True


def test_wild_draw4_to_action_card():
    wild_draw4_to_action_card_args = {"card_1": wild_draw4, "card_2": draw2_red}
    assert Rule("number_f", rule_wild_card, wild_draw4_to_action_card_args).check() is True


def test_wild_normal_to_number_card():
    wild_normal_to_number_card_args = {"card_1": wild_normal, "card_2": red_1}
    assert Rule("number_g", rule_wild_card, wild_normal_to_number_card_args).check() is True


def test_wild_normal_to_action_card():
    wild_normal_to_action_card_args = {"card_1": wild_normal, "card_2": draw2_red}
    assert Rule("number_h", rule_wild_card, wild_normal_to_action_card_args).check() is True
