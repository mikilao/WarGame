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

roundCounter = 1
while winner == False:
    print("Round ")
    print(roundCounter)
    if len(player_1) == 0:
        print("Player 1 wins the game")
        winner == True
    if len(player_2) == 0:
        print("Player 2 wins the game")
        winner == True
    if player_1[0] > player_2[0]:
        print("Player 1 wins")

        player_1.append(player_2[0])
        player_2.pop(0)
        player_1.append(player_1[0])
        player_1.pop(0)
    if player_2[0] > player_1[0]:
        print("Player 2 wins!")
        player_2.append(player_1[0])
        player_1.pop(0)
        player_2.append(player_2[0])
        player_2.pop(0)
    roundCounter = roundCounter+1
