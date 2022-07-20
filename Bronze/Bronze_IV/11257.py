N = int(input())

for _ in range(N):
    tester, one, two, three = map(int, input().split())
    if one >= 10.5 and two >= 7.5 and three >= 12 and sum([one, two, three]) >= 55:
        print(tester, sum([one, two, three]), "PASS")
    else:
        print(tester, sum([one, two, three]), "FAIL")