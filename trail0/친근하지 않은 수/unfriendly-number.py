N = int(input())
arr = []
for num in range(1, N+1):
    if num % 2 == 0:
        continue
    elif num % 3 == 0:
        continue
    elif num % 5 == 0:
        continue
    else:
        arr.append(num)

print(len(arr))
