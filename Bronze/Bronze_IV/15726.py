A, B, C = map(int, input().split())

a = (A * B) / C
b = (A / B) * C

print(max(int(a), int(b)))