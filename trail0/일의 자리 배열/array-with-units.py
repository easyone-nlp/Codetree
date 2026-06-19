A, B = map(int, input().split())

C = []

for i in range(10):
    if i == 0:
        C.append(A)
    elif i == 1:    
        C.append(B)
    else:
        C.append((C[i-2]+C[i-1]) % 10)
    print(C[i], end=" ")