students = [0 for x in range(31)]

for i in range(1, 29):
    n = int(input())
    students[n] = 1

for i in range(len(students)):
    if i == 0:
        continue
    if students[i] == 0:
        print(i)