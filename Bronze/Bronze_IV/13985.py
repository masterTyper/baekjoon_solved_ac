data, result = map(str, input().split(' = '))

if int(eval(data)) == int(result):
    print('YES')
else:
    print('NO')