N, M = map(int, input().split())

arr1 = []
arr2 = []
for _ in range(N):
    nums = list(map(int, input().split()))
    arr1.append(nums)

for _ in range(N):
    nums = list(map(int, input().split()))
    arr2.append(nums)

for i in range(N):
    for j in range(M):
        print(arr1[i][j] + arr2[i][j], end=" ")
    print()