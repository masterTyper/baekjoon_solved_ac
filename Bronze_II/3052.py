remains = []
for i in range(10):
    num = int(input())
    remains.append(num % 42)

remains = set(remains)
print(len(remains))