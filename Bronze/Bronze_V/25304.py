X = int(input())
N = int(input())

cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    c = a * b
    cnt += c

if cnt == X:
    print("Yes")
else:
    print("No")