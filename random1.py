import random   # Simple random library example

'''
choice
'''
coin = random.choice(["heads", "tails"])
print(coin)

'''
Also written as

from random import choice  # here we are importing the choice module form import instead of calling out every time in below

coin = choice(["heads", "tails"])   # here we removed the random
print(coin)

'''

'''
randint
'''

number = random.randint(1,10)  # printing random int between 1 an 10 
print(number)

'''
shuffle
'''

cards = ["jack", "queen", "king"]   # Listing the values
random.shuffle(cards)               # random shuffle - this function shuffles and gives in random order
for card in cards:                  # here we are using loop to present cards one by one instead of all in one list of shuffled manner
    print(card) 