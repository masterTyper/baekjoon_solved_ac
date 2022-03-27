from collections import Counter

x = []
y = []
for i in range(3):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)

print(Counter(x).most_common()[1][0], Counter(y).most_common()[1][0])

