A, B, C = map(int, input().split())
num1, num2 = 0, 0

for e in [A, B, C]:
    if e == 1:
        num1 += 1
    if e == 2:
        num2 += 1

if num1 > num2:
    print(1)
else:
    print(2)
