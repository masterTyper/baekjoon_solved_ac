import math

X, L, R = map(int, input().split())

mini = math.inf
c = 0

for x in range(L, R + 1, 1):
    if mini > abs(X - x):
        mini = abs(X - x)
        c = x

print(c)