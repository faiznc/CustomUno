from Game.rules import rule_color_states, Rule
from card_objects import *


def test_color_to_number_different_color_1():
    color_to_number_args = {"card_1": virt_color_red, "card_2": green_1}
    assert Rule("color_a1", rule_color_states, color_to_number_args).check() is False


def test_color_to_number_different_color_2():
    color_to_number_args = {"card_1": virt_color_red, "card_2": green_2}
    assert Rule("color_a2", rule_color_states, color_to_number_args).check() is False


def test_color_to_number_same_color_1():
    color_to_number_args = {"card_1": virt_color_red, "card_2": red_1}
    assert Rule("color_b1", rule_color_states, color_to_number_args).check() is True


def test_color_to_number_same_color_2():
    color_to_number_args = {"card_1": virt_color_red, "card_2": red_2}
    assert Rule("color_b2", rule_color_states, color_to_number_args).check() is True


def test_color_to_skip_different_color_1():
    color_to_skip_args = {"card_1": virt_color_red, "card_2": skip_green}
    assert Rule("color_d1", rule_color_states, color_to_skip_args).check() is False


def test_color_to_skip_different_color_2():
    color_to_skip_args = {"card_1": virt_color_green, "card_2": skip_red}
    assert Rule("color_d2", rule_color_states, color_to_skip_args).check() is False


def test_color_to_skip_same_color_1():
    color_to_skip_args = {"card_1": virt_color_red, "card_2": skip_red}
    assert Rule("color_c1", rule_color_states, color_to_skip_args).check() is True


def test_color_to_skip_same_color_2():
    color_to_skip_args = {"card_1": virt_color_green, "card_2": skip_green}
    assert Rule("color_c2", rule_color_states, color_to_skip_args).check() is True


def test_color_to_reverse_different_color_1():
    color_to_reverse_args = {"card_1": virt_color_red, "card_2": reverse_green}
    assert Rule("color_e1", rule_color_states, color_to_reverse_args).check() is False


def test_color_to_reverse_different_color_2():
    color_to_reverse_args = {"card_1": virt_color_green, "card_2": reverse_red}
    assert Rule("color_e2", rule_color_states, color_to_reverse_args).check() is False


def test_color_to_reverse_same_color_1():
    color_to_reverse_args = {"card_1": virt_color_red, "card_2": reverse_red}
    assert Rule("color_f1", rule_color_states, color_to_reverse_args).check() is True


def test_color_to_reverse_same_color_2():
    color_to_reverse_args = {"card_1": virt_color_green, "card_2": reverse_green}
    assert Rule("color_f2", rule_color_states, color_to_reverse_args).check() is True


def test_color_to_draw_different_color_1():
    color_to_draw_args = {"card_1": virt_color_red, "card_2": draw2_green}
    assert Rule("color_g1", rule_color_states, color_to_draw_args).check() is False


def test_color_to_draw_different_color_2():
    color_to_draw_args = {"card_1": virt_color_green, "card_2": draw2_red}
    assert Rule("color_g2", rule_color_states, color_to_draw_args).check() is False


def test_color_to_draw_same_color_1():
    color_to_draw_args = {"card_1": virt_color_red, "card_2": draw2_red}
    assert Rule("color_h1", rule_color_states, color_to_draw_args).check() is True


def test_color_to_draw_same_color_2():
    color_to_draw_args = {"card_1": virt_color_green, "card_2": draw2_green}
    assert Rule("color_h2", rule_color_states, color_to_draw_args).check() is True


def test_color_to_wild_draw4():
    color_to_wild_args = {"card_1": virt_color_red, "card_2": wild_draw4}
    assert Rule("color_i", rule_color_states, color_to_wild_args).check() is True


def test_color_to_normal_wild():
    color_to_normal_wild_args = {"card_1": virt_color_red, "card_2": wild_normal}
    assert Rule("color_j", rule_color_states, color_to_normal_wild_args).check() is True
