a, b, c = map(int, input().split())

numbers = [a, b, c]
numbers.sort()

print(" ".join(str(number) for number in numbers))

