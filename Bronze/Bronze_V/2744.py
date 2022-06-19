S = input()

word = ""
for i in S:
    if i.isupper():
        word += i.lower()
    if i.islower():
        word += i.upper()

print(word)