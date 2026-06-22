N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i-1
    for j in range(i):
        print(j+1 + (sum), end=" ")
    print()