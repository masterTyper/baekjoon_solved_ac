T = int(input())

for i in range(T):
    n = int(input())
    n_list = list(str(bin(n)[2:][::-1]))
    index = []
    for j in range(len(n_list)):
        if n_list[j] == '1':
            index.append(str(j))
    print(" ".join(index))
