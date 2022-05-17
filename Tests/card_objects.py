from CardObjects.card import NumberCard, ActionCard, WildCard, ColorCard

red_1 = NumberCard(1, "red")
red_2 = NumberCard(2, "red")
red_3 = NumberCard(3, "red")
green_1 = NumberCard(1, "green")
green_2 = NumberCard(2, "green")

draw2_red = ActionCard("Draw2", "red")
draw2_green = ActionCard("Draw2", "green")
skip_red = ActionCard("Skip", "red")
skip_green = ActionCard("Skip", "green")
reverse_red = ActionCard("Reverse", "red")
reverse_green = ActionCard("Reverse", "green")
reverse_yellow = ActionCard("Reverse", "yellow")

wild_draw4 = WildCard("Draw4", 10)
wild_normal = WildCard("Wild", 5)

virt_color_red = ColorCard("red")
virt_color_green = ColorCard("green")