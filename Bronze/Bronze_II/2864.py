A, B = map(str, input().split())

A_min = str(A).replace('6', '5')
B_min = str(B).replace('6', '5')

A_max = str(A).replace('5', '6')
B_max = str(B).replace('5', '6')

print(int(A_min) + int(B_min), int(A_max) + int(B_max))