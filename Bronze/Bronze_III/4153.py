while True:
    lines = list(map(int, input().split()))

    if lines[0] == 0 and lines[1] == 0 and lines[2] == 0:
        break

    c = max(lines)
    a = min(lines)
    lines.remove(c)
    lines.remove(a)
    b = lines[0]

    if c ** 2 == a ** 2 + b ** 2:
        print("right")
    else:
        print("wrong")
