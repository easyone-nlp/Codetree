
while True:
    num = int(input().strip())

    if num < 25:
        print("Higher")
    elif num > 25:
        print("Lower")
    elif num == 25:
        print("Good")
        break