a = list(map(int, input().split()))
c = list(map(int, input().split()))

bx = c[0] - a[2]
by = c[1] // a[1]
bz = c[2] - a[0]

print(bx, by, bz)