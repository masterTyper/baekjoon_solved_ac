S = input()

if len(S) == 4:
    print(20)
if len(S) == 3:
    if S[1] == '0':
        print(int(S[:2]) + int(S[-1]))
    else:
        print(int(S[0]) + int(S[1:]))
if len(S) == 2:
    print(int(S[0]) + int(S[-1]))
