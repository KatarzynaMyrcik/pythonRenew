import random


class Dice:
#it has to be a tuple of 2 random values
    def roll(self):
        lista = []
        for i in range(2):
            value = random.randint(1,6)
            lista.append(value)
        result = tuple(lista)
        return result


result = Dice()
score = result.roll()
print(score)


"""MOsh:
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())
"""
