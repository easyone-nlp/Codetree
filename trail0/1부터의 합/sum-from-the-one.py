N = int(input())
sum = 0
for num in range(1, 101):
    sum += num
    if sum >= N:
        print(num)
        break