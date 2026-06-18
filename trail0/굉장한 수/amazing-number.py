n = int(input())


if (n % 2 == 1) & (n % 3 == 0):
    print("true")
elif (n % 2 == 0) & (n % 5 == 0):
    print("true")
else:
    print("false")
