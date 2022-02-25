import sys
from collections import Counter

N = int(sys.stdin.readline().strip())

nums = []
for i in range(N):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

nums.sort()

print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])

counts = Counter(nums).most_common()
if len(counts) > 1:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])

print(max(nums) - min(nums))
