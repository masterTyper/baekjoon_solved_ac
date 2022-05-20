sum = 0
for i in range(5):
    score = int(input())
    if score < 40:
        sum += 40
        continue
    sum += score

avg = sum // 5

print(avg)

