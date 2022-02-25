N = int(input())

cnt = 1
num = 666
while True:
    if N == cnt:
        print(num)
        break
    else:
        num += 1
        if '666' in str(num):
            cnt += 1