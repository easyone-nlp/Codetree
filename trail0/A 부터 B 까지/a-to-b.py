A, B = map(int, input().split())
num = A

while num <= B:
    print(num, end=" ")
    if num % 2 == 1:
        num *= 2
    else:
        num += 3
    