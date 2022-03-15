T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print("Case #{x}: {a} + {b} = {c}".format(x=(i + 1), a=A, b=B, c=(A + B)))
