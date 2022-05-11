from CardObjects.card import NumberCard, ActionCard, WildCard

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
