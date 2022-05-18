from Game.rules import rule_action_card, Rule
from card_objects import *


def test_skip_to_number_same_color():
    skip_to_number_same_color_args = {"card_1": skip_red, "card_2": red_1}
    assert Rule("action_a", rule_action_card, skip_to_number_same_color_args).check() is True


def test_skip_to_number_different_color():
    skip_to_number_different_color_args = {"card_1": skip_red, "card_2": green_1}
    assert Rule("action_b", rule_action_card, skip_to_number_different_color_args).check() is False


def test_skip_to_skip_different_color():
    skip_to_skip_different_color_args = {"card_1": skip_red, "card_2": skip_green}
    assert Rule("action_e", rule_action_card, skip_to_skip_different_color_args).check() is True


def test_skip_to_skip_same_card():
    skip_to_skip_same_card_args = {"card_1": skip_red, "card_2": skip_red}
    assert Rule("action_h", rule_action_card, skip_to_skip_same_card_args).check() is True


def test_skip_to_reverse_same_color():
    skip_to_reverse_same_color_args = {"card_1": skip_red, "card_2": reverse_red}
    assert Rule("action_f", rule_action_card, skip_to_reverse_same_color_args).check() is True


def test_skip_to_reverse_different_color():
    skip_to_reverse_different_color_args = {"card_1": skip_red, "card_2": reverse_green}
    assert Rule("action_g", rule_action_card, skip_to_reverse_different_color_args).check() is False


def test_skip_to_draw2_same_color():
    skip_to_draw2_same_color_args = {"card_1": skip_red, "card_2": draw2_red}
    assert Rule("action_i", rule_action_card, skip_to_draw2_same_color_args).check() is True


def test_skip_to_draw2_different_color():
    skip_to_draw2_different_color_args = {"card_1": skip_red, "card_2": draw2_green}
    assert Rule("action_j", rule_action_card, skip_to_draw2_different_color_args).check() is False


def test_skip_to_wildcard():
    skip_to_wildcard_args = {"card_1": skip_red, "card_2": wild_normal}
    assert Rule("action_c", rule_action_card, skip_to_wildcard_args).check() is True


def test_skip_to_draw4():
    skip_to_draw4_args = {"card_1": skip_red, "card_2": wild_draw4}
    assert Rule("action_d", rule_action_card, skip_to_draw4_args).check() is True


def test_reverse_to_number_same_color():
    reverse_to_number_same_color_args = {"card_1": reverse_red, "card_2": red_1}
    assert Rule("action_k", rule_action_card, reverse_to_number_same_color_args).check() is True


def test_reverse_to_number_different_color():
    reverse_to_number_different_color_args = {"card_1": reverse_red, "card_2": green_1}
    assert Rule("action_l", rule_action_card, reverse_to_number_different_color_args).check() is False


def test_reverse_to_skip_same_color():
    reverse_to_skip_same_color_args = {"card_1": reverse_red, "card_2": skip_red}
    assert Rule("action_n", rule_action_card, reverse_to_skip_same_color_args).check() is True


def test_reverse_to_skip_different_color():
    reverse_to_skip_different_color_args = {"card_1": reverse_red, "card_2": skip_green}
    assert Rule("action_m", rule_action_card, reverse_to_skip_different_color_args).check() is False


def test_reverse_to_draw2_same_color():
    reverse_to_draw2_same_color_args = {"card_1": reverse_red, "card_2": draw2_red}
    assert Rule("action_o", rule_action_card, reverse_to_draw2_same_color_args).check() is True


def test_reverse_to_draw2_different_color():
    reverse_to_draw2_different_color_args = {"card_1": reverse_red, "card_2": draw2_green}
    assert Rule("action_p", rule_action_card, reverse_to_draw2_different_color_args).check() is False


def test_reverse_to_wildcard():
    reverse_to_wildcard_args = {"card_1": reverse_red, "card_2": wild_normal}
    assert Rule("action_q", rule_action_card, reverse_to_wildcard_args).check() is True


def test_reverse_to_draw4():
    reverse_to_draw4_args = {"card_1": reverse_red, "card_2": wild_draw4}
    assert Rule("action_r", rule_action_card, reverse_to_draw4_args).check() is True


def test_draw2_to_number_same_color():
    draw2_to_number_same_color_args = {"card_1": draw2_red, "card_2": red_1}
    assert Rule("action_s", rule_action_card, draw2_to_number_same_color_args).check() is True


def test_draw2_to_number_different_color():
    draw2_to_number_different_color_args = {"card_1": draw2_red, "card_2": green_1}
    assert Rule("action_t", rule_action_card, draw2_to_number_different_color_args).check() is False


def test_draw2_to_skip_same_color():
    draw2_to_skip_same_color_args = {"card_1": draw2_red, "card_2": skip_red}
    assert Rule("action_v", rule_action_card, draw2_to_skip_same_color_args).check() is True


def test_draw2_to_skip_different_color():
    draw2_to_skip_different_color_args = {"card_1": draw2_red, "card_2": skip_green}
    assert Rule("action_u", rule_action_card, draw2_to_skip_different_color_args).check() is False


def test_draw2_to_draw2_same_color():
    draw2_to_draw2_same_color_args = {"card_1": draw2_red, "card_2": draw2_red}
    assert Rule("action_w", rule_action_card, draw2_to_draw2_same_color_args).check() is True


def test_draw2_to_draw2_different_color():
    draw2_to_draw2_different_color_args = {"card_1": draw2_red, "card_2": draw2_green}
    assert Rule("action_x", rule_action_card, draw2_to_draw2_different_color_args).check() is True


def test_draw2_to_reverse_same_color():
    draw2_to_reverse_same_color_args = {"card_1": draw2_red, "card_2": reverse_red}
    assert Rule("action_y", rule_action_card, draw2_to_reverse_same_color_args).check() is True


def test_draw2_to_reverse_different_color():
    draw2_to_reverse_different_color_args = {"card_1": draw2_red, "card_2": reverse_green}
    assert Rule("action_z", rule_action_card, draw2_to_reverse_different_color_args).check() is False


def test_draw2_to_wildcard():
    draw2_to_wildcard_args = {"card_1": draw2_red, "card_2": wild_normal}
    assert Rule("action_aa", rule_action_card, draw2_to_wildcard_args).check() is True


# TODO : Failed on this test
def test_draw2_to_draw4():
    draw2_to_draw4_args = {"card_1": draw2_red, "card_2": wild_draw4}
    assert Rule("action_ab", rule_action_card, draw2_to_draw4_args).check() is True
