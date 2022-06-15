N = int(input())
honey = list(map(int, input().split()))

sum = honey.copy()

result = 0
for i in range(1, N):
    sum[i] += sum[i - 1]

for i in range(1, N - 1):
    result = max(result, sum[N - 2] + sum[i - 1] - honey[i])
    result = max(result, sum[N - 1] - honey[0] + sum[N - 1] - sum[i] - honey[i])
    result = max(result, sum[N - 2] - honey[0] + honey[i])

print(result)
