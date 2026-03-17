import random


#random.choice(seq) is a function that takes a list as an argument and returns a random element from that list.
coin = random.choice(["heads", "tails"])

print(coin)

#random.randint(a, b) is a function that takes two integers as arguments and returns a random integer between those two integers (inclusive).
random_number = random.randint(1, 10)
print(random_number)

#random.shuffle(seq) is a function that takes a list as an argument and shuffles the elements of that list in place.
cards = ["ace", "king", "queen", "jack", "10"]
random.shuffle(cards)
print(cards)