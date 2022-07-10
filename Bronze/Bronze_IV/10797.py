day = int(input())
car_nums = list(map(int, input().split()))

cnt = 0
for num in car_nums:
    if day == num:
        cnt += 1

print(cnt)