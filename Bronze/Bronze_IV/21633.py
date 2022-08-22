k = int(input())

tugriks = ((k / 100) + 25)
if tugriks < 100:
    print(format(100.00, ".2f"))
elif tugriks <= 2000:
    print(format(tugriks, ".2f"))
else:
    print(format(2000.00, ".2f"))