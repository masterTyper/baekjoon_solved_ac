from collections import Counter

N = int(input())
nums_N = list(map(int, input().split()))
M = int(input())
nums_M = list(map(int, input().split()))

counter = Counter(nums_N)

result = []

for num in nums_M:
    if num in counter:
        result.append(str(counter.get(num)))
    else:
        result.append(str(0))

print(" ".join(result))
