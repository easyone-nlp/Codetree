A, B, C = map(int, input().split(" "))

if A > B:
    if B > C:
        print(B)
    elif A < C:
        print(A)
    else:
        print(C)
elif A < B:
    if B < C:
        print(B)
    elif C < A:
        print(A)
    else:
        print(C)