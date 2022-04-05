chess_input = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

result = []
for i in range(len(chess)):
    result.append(chess[i] - chess_input[i])

print(" ".join(map(str, result)))
