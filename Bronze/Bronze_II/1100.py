fields = []
for i in range(8):
    field = input()
    fields.append(field)

sum = 0
for i in range(len(fields)):
    if i % 2 == 0:
        for j in range(len(fields[i])):
            if j % 2 == 0 and fields[i][j] == 'F':
                sum += 1
    else:
        for j in range(len(fields[i])):
            if j % 2 == 1 and fields[i][j] == 'F':
                sum += 1

print(sum)