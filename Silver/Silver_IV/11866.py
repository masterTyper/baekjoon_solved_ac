from collections import deque

N, K = map(int, input().split())

queue = deque()
nums = []

for i in range(1, N + 1):
    queue.append(i)

while queue:
    for i in range(K - 1):
        queue.append(queue[0])
        queue.popleft()
    nums.append(str(queue.popleft()))

print("<" + ", ".join(nums) + ">")