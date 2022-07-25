from collections import Counter

T = int(input())

teas = Counter(list(map(int, input().split())))
print(teas[T])