n = int(input())

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

def lcm(m, n):
    return (m * n) // gcd(m, n)

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
