N, X = map(int, input().split())

A = list(map(int, input().split()))

nums = []
for i in range(N):
    if A[i] < X:
        nums.append(A[i])

print(' '.join(map(str, nums)))