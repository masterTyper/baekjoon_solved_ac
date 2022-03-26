N = int(input())

nums = list(map(int, input().split()))
set_nums = list(sorted(set(nums)))

dic = {set_nums[i]: i for i in range(len(set_nums))}

for i in nums:
    print(dic[i], end=' ')
