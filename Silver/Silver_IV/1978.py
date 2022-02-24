N = int(input())
nums = list(map(int, input().split()))

def prime_number(num):
    if num == 1:
        return False
    for i in range(num):
        if i != 0 and i != 1:
            if num % i == 0:
                return False
    return True

sum = 0
for num in nums:
    if prime_number(num):
       sum += 1

print(sum)