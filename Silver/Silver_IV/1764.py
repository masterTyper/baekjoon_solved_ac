N, M = map(int, input().split())

set_a = set()
for i in range(N):
    set_a.add(input())

set_b = set()
for i in range(M):
    set_b.add(input())

result = sorted(list(set_a & set_b))

print(len(result))
for i in range(len(result)):
    print(result[i])
