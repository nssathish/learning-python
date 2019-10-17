import random


class Dice:
    def __init__(self, dice_min, dice_max):
        self.dice_min = dice_min
        self.dice_max = dice_max
        self.dice2_value = random.randint(self.dice_min, self.dice_max)
        self.dice1_value = random.randint(self.dice_min, self.dice_max)

    def roll(self):
        return self.dice1_value, self.dice2_value


dices = Dice(1, 6)
print(dices.roll())
