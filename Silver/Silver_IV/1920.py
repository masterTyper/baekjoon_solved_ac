import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

E = list(map(int, sys.stdin.readline().split()))

A.sort()


def binary_search(target):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == target:
            return True
        elif A[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


for i in range(M):
    if binary_search(E[i]):
        print(1)
    else:
        print(0)
