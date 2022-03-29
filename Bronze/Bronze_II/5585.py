money = int(input())

money = 1000 - money

fh = money // 500
money = money - fh * 500

oh = money // 100
money = money - oh * 100

fy = money // 50
money = money - fy * 50

ten = money // 10
money = money - ten * 10

five = money // 5
money = money - five * 5

one = money
money = money - one

print(fh + oh + fy + ten + five + one)
