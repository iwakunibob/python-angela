# Black Jack Game Project by Robert Laurie
import art
import random

suits = ['\u2666', '\u2665',  '\u2660', '\u2663']
ranks = ['2', '3', '4', '5', '6', '7',
         '8', '9', 'T', 'J', 'Q', 'K', 'A']
deck = []
dealer = []
gambler = []
print(art.logo)
print("Welcome to the Black Jack Game")
print(suits)
print(ranks)
for suit in suits:
    for rank in ranks:
      deck.append(rank + suit)
print(deck)
random.shuffle(deck)
print(deck)
for i in range(2):
    gambler.append(deck.pop(0))
    dealer.append(deck.pop(0))
print(f"Dealer Card Showing is {dealer[0]}")
print(f"Gambler Cards are: {gambler[0]} and {gambler[1]}")
