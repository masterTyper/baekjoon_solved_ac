N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda n:(n[0], n[1]))

for point in points:
    print(point[0], point[1])