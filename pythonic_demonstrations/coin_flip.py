from random import random

def flip_coin():
    #generate a random number 0-1
    r = random()
    if r > 0.5:
        return "heads"
    else:
        return "tails"

print (flip_coin())