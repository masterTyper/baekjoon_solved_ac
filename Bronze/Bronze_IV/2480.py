from collections import Counter

dice = list(map(int, input().split()))

counter = Counter(dice)

for i in range(1, 7):
    if counter[i] == 3:
        print(10000 + i * 1000)
    if counter[i] == 2:
        print(1000 + i * 100)

if len(set(dice)) == 3:
    print(max(dice) * 100)
