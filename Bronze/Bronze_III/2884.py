H, M = map(int, input().split())

m = M - 45

if m < 0:
    H -= 1
    if H == -1:
        H = 23
    m = 60 + m

print(H, m)
