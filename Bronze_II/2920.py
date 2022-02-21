melody = list(map(int, input().split()))
origin = [1, 2, 3, 4, 5, 6, 7, 8]
if melody == sorted(origin):
    print("ascending")
elif melody == list(reversed(origin)):
    print("descending")
else:
    print("mixed")