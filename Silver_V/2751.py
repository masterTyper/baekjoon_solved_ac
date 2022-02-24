N = int(input())

numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

for number in numbers:
    print(number)