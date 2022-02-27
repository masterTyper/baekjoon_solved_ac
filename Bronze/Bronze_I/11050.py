N, K = map(int, input().split())

def factorial(n):
    mul = 1
    for i in range(n, 0, -1):
        mul *= i
    return mul


N_fac = factorial(N)
K_fac = factorial(K)
NK_fac = factorial(N - K)

print(int(N_fac / (K_fac * NK_fac)))
