import Game.engine

from Game.engine import Orchestrator
from Game.player import Player
from Game.rules import Rule
from Game.rules import *

GameState = ["START", "PLAY", "END"]
# In the future, there will be current color and current number
# There are also last action (Higher Priority), allowed card types
# which can be used to decide the next action


red_1 = NumberCard(1, "red")
red_2 = NumberCard(2, "red")

rule_actions = Rule("Actions", Game.rules.rule_action_card)
rule_numbers = Rule("Numbers", Game.rules.rule_number_card)
rule_wilds = Rule("Wilds", Game.rules.rule_wild_card)
rule_colors = Rule("Colors", Game.rules.rule_color_states)

rule_sets = [rule_actions, rule_numbers, rule_wilds, rule_colors]

controller = Orchestrator(rule_sets)
controller.set_current_card(red_1)

player_1 = Player(controller, "Player 1")
player_2 = Player(controller, "Player 2")

player_list = [player_1, player_2]

player_1.add_card(red_1)
player_1.add_card(red_1)
player_1.add_card(red_1)

print(player_1.get_current_cards())

# controller.handle_card_proposal(player_1, red_2)
# a = controller.handle_card_proposal(red_2)
# print(a)