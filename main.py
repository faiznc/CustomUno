import Game.engine
from CardObjects.card import NumberCard

from Game.engine import Orchestrator
from Game.engine import Rule
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

# rule_lists = [rule_number_card, rule_action_card, rule_wild_card, rule_color_states]

rule_lists = [rule_actions, rule_numbers, rule_wilds, rule_colors]

controller = Orchestrator(rule_lists)


controller.set_current_card(red_1)

result = controller.check_card_proposal(red_2)
print(result)
