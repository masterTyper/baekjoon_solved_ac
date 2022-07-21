while True:
    letter = input()
    if letter == "END":
        break
    else:
        print(letter[::-1])