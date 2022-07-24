arr = list(map(int, input().split()))

max = max(arr)
arr.remove(max)

min = min(arr)
arr.remove(min)

print(arr[0])