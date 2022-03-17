N = int(input())

def summation(arr):
    sum = 0
    result = 0
    for i in arr:
        for j in range(1, len(i)+1):
            sum += j
        result += sum
        sum = 0
    return result

for i in range(N):
    ox = input()
    question = list(filter(None, ox.split('X')))
    print(summation(question))
