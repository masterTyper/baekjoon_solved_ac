from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_combinations = combinations(cards, 3)

big_sum = 0
for combination in cards_combinations:
    temp_sum = sum(combination)
    if big_sum < temp_sum <= M:
        big_sum = temp_sum

print(big_sum)
