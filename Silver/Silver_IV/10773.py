K = int(input())

nums = []
for i in range(K):
    num = int(input())
    if num == 0:
        try:
            nums.pop()
        except:
            exit()
    else:
        nums.append(num)

print(sum(nums))
