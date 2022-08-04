number = int(input())

for i in range(number):
    steps = list(input())
    cnt = 0
    for step in steps:
        if step == "U":
            cnt += 1
        if step == "D":
            break
    print(cnt)
