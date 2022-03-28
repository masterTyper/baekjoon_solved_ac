T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    XX = "0" + str(N // H + 1) if len(str(N // H + 1)) == 1 else str(N // H + 1)
    YY = str(N % H)

    if N % H == 0:
        XX = "0" + str(N // H) if len(str(N // H)) == 1 else str(N // H)
        YY = str(H)

    room = YY + XX

    print(room)