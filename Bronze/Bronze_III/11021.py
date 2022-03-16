T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print("Case #{x}: {y}".format(x=(i + 1), y=(A + B)))
