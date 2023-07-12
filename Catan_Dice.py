import random


class Dice:
    def roll(self):
        event_list = ["Pirates", "Blue", "Yellow", "Green"]
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.choice(event_list)
        print(f"""
Red Dice: {dice1} 
Yellow Dice: {dice2}
Event Dice: {dice3}
""")


dice = Dice()
dice.roll()
