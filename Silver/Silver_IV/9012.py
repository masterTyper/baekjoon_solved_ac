N = int(input())

def VPS(parens):
    for paren in parens:
        if paren[0] == ')' or paren[-1] == '(':
            print("NO")
            continue
        else:
            temp = []
            for i in range(len(paren)):
                if paren[i] == '(':
                    temp.append(paren[i])
                elif paren[i] == ')':
                    if len(temp) != 0 and temp[-1] == '(':
                        temp.pop()
                    else:
                        temp.append(paren[i])
                        break
            if len(temp) == 0:
                print("YES")
            else:
                print("NO")

parens = []
for i in range(N):
    paren = input()
    parens.append(paren)

VPS(parens)