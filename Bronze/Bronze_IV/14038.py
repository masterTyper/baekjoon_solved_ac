cnt = 0

for i in range(6):
    game = input()
    if game == 'W':
        cnt += 1
    else:
        pass
    if i == 5:
        if cnt == 0:
            print(-1)
        if cnt == 1 or cnt == 2:
            print(3)
        if cnt == 3 or cnt == 4:
            print(2)
        if cnt == 5 or cnt == 6:
            print(1)