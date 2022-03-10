A, B = map(int, input().split())
C = int(input())

h = C // 60 + A
m = C % 60 + B

if m >= 60:
    h += 1
    m = m % 60

if h >= 24:
    h -= 24

print(h, m)
