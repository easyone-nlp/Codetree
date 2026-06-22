start, end = map(int, input().split())

cnt = 0

for num in range(start, end+1):
    arr = []
    for i in range(1, num+1):
        if num % i == 0:
            arr.append(i)
    if len(arr) == 3:
        cnt += 1
print(cnt)