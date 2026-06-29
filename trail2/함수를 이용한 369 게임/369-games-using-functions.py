a, b = map(int, input().split())

cnt = 0

# def three_six_nine(i):
#     num_1 = i % 10
#     num_2 = i // 10
#     num_3 = i // 100
#     num_4 = i // 1000
#     num_5 = i // 10000
#     num_6 = i // 100000
#     num_7 = i // 1000000
#     return (num_1 in [3, 6, 9]) or (num_2 in [3, 6, 9]) or (num_3 in [3, 6, 9]) or (num_4 in [3, 6, 9]) or (num_5 in [3, 6, 9]) or (num_6 in [3, 6, 9]) or (num_7 in [3, 6, 9])

def three_six_nine(i):
    return '3' in str(i) or '6' in str(i) or '9' in str(i)

def magic_num(i):
    return i % 3 == 0

for n in range(a, b+1):
    if three_six_nine(n) or magic_num(n):
        cnt += 1

print(cnt)