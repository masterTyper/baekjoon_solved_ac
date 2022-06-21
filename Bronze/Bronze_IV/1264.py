while True:
    cnt = 0
    string = input()
    if string == "#":
        exit()
    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1
    print(cnt)
