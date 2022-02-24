N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda n:(n[1], n[0]))

for point in points:
    print(point[0], point[1])