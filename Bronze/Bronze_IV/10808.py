S = input()
cnt = [0] * 26

for c in S:
    cnt[ord(c)-97] += 1

print(*cnt)