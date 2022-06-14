N, M = map(int, input().split())

dic = {}
for _ in range(N):
    key = input()
    dic[key] = True

cnt = 0
for _ in range(M):
    string = input()
    try:
        if dic[string]:
            cnt += 1
    except:
        pass

print(cnt)