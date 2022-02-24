from collections import deque

def logic(cards):
    cards.popleft()
    pop_left = cards.popleft()
    cards.append(pop_left)
    return cards

N = int(input())

cards = deque()
for i in range(1, N + 1):
    cards.append(i)

while True:
    if len(cards) == 1:
        print(cards[0])
        break
    cards = logic(cards)