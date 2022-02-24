valid_nums = list(map(int, input().split()))
sum = 0
for num in valid_nums:
    sum += num ** 2
print(sum % 10)