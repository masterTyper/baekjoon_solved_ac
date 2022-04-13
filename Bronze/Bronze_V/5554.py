import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())

sec = sum([A, B, C, D])
minutes = sec // 60
seconds = sec % 60

print(minutes)
print(seconds)

