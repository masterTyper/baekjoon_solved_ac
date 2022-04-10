import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

counter = Counter(arr)

idx = [0] * (max(counter) + 1)

for i in range(1, max(counter) + 1):
    idx[i] = counter[i]

sum1 = 0
ans1 = 1
mini_sum1 = 999999999999999999999
sum2 = 0
ans2 = 1
mini_sum2 = 999999999999999999999
for i in range(1, len(idx)):
    sum1 = 0
    sum2 = 0
    for j in range(1, len(idx)):
        sum1 += abs(i - j) * idx[j]
        sum2 += (abs(i - j) ** 2) * idx[j]
    if sum1 < mini_sum1:
        mini_sum1 = sum1
        ans1 = i
    if sum2 < mini_sum2:
        mini_sum2 = sum2
        ans2 = i

print(ans1, ans2)