N, M = map(int, input().split())

if M == 1 or M == 2:
    print('NEWBIE!')

elif 2 < M <= N:
    print("OLDBIE!")

else:
    print("TLE!")
