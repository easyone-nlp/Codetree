N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    total = 0
    for num in range(a, b+1):
        if num % 2 == 0:
            total += num
    print(total)