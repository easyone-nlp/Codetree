arr = [int(input()) for i in range(1, 11) ]

# print(arr)

cnt1 = 0
cnt2 = 0
for a in arr:
    if a % 3 == 0:
        cnt1 += 1
    if a % 5 == 0:
        cnt2 += 1

print(cnt1, cnt2)