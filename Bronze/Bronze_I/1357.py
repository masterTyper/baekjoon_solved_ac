X, Y = input().split()
rev_X = X[::-1]
rev_Y = Y[::-1]
sum = int(rev_X) + int(rev_Y)
print(int(str(sum)[::-1]))