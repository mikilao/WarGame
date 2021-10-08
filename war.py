import random

player_1 = []
player_2 = []

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
winner = False


random.shuffle(deck)
half_hand = (len(deck) / 2)
half = int(half_hand)
for x in range(0, half):
    player_1.append(deck[x])
print(player_1)
for y in range(half, len(deck)):
    player_2.append(deck[y])
print(player_2)
# while winner == False:
