A, B = map(int, input().split())

nums = []
for i in range(1, B + 1):
    for j in range(i):
        nums.append(i)

A = A - 1
sum = 0
for i in range(A, B):
    sum += nums[i]

print(sum)