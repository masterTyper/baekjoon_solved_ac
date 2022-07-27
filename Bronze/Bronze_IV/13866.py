skills = list(map(int, input().split()))

print(abs(2 * (max(skills) + min(skills)) - sum(skills)))