N = int(input())
A = list(set(map(int, input().split())))

def is_prime(num):
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


primes =[]
for i in range(len(A)):
    if is_prime(A[i]):
        primes.append(A[i])

lcm = 1
for prime in primes:
    lcm *= prime

if lcm == 1:
    print(-1)
else:
    print(lcm)
