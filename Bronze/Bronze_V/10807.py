from collections import Counter

N = int(input())
nums = Counter(list(map(int, input().split())))
v = int(input())

print(nums[v])