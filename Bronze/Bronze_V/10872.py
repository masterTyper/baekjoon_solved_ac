N = int(input())

fac = range(1, N + 1)
cnt = 1

for i in fac:
    cnt *= i

print(cnt)