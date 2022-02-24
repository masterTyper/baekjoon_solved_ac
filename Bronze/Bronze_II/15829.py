alphabet = [chr(x) for x in range(97, 123)]

L = int(input())
if L == 0:
    print(0)
    exit()
string = input()

sum = 0
if len(string) == L:
    for i in range(len(string)):
        sum += (alphabet.index(string[i]) + 1) * (31 ** i)

print(sum % 1234567891)